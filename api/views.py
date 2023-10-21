from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import null
from .models import Items as ItemsStore,Products as ProductsStore,Sells as SellsStore,Sizes as SizesStore, Brands as BrandsStore  
from api.ecommerce.models import ProductStocks as ProductStocksEcommerce,OrderDetails as OrderDetailsEcommerce,Products as ProductsEcommerce, Brands as BrandsEcommerce
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


class ScrapView(APIView):
    
    def get(self,request):
        
        items = ItemsStore.objects.all();
        for item in items:
            products = ProductsEcommerce.objects.get(id=item.pid);
            products.itemid = item.itemid;
            print(f'{item.itemname} and {products.name}')


        url = request.GET['url']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }


        page = requests.get(url,headers=headers)

        soup = BeautifulSoup(page.content,'html.parser')

        description = ''

        try:
            tbody = soup.select('tbody')[1]
            count = 0
            for e in tbody:
                # print(e,count)
                if count == 3:
                    data1 = e.find("span").string;

                if count == 7:
                    data2 = e.find("span").string;
                    
                if count == 9:
                    data3 = e.find("span").string;
                count+=1

            data = data1 +'\n'+ data2 +'\n'+ data3+'\n'
        except Exception as e:
            return Response({
                'success':False,
                'message':str(e)
            })


        return Response({
                'success':True,
                'data':data
            })


class ProductsView(APIView):
    
    def get(self,request):
        three_days = datetime.now() - timedelta(hours=72)
        twenty_days = datetime.now() - timedelta(hours=480)
        exclude_list = ['cancel','delivered','picked_up','on_the_way']
        resp = ''

        try:
            stocks = ProductStocksEcommerce.objects.all().using("ecommerce")
            for stk in stocks:
                pid = stk.product_id
                variant = stk.variant
                try:
                    products_ecommerce = ProductsEcommerce.objects.using("ecommerce").get(id=pid)
                    item_id_store = products_ecommerce.item_id
                    if products_ecommerce is None:
                        continue
                    
                    try:
                        product_quantity_final = 0
                        product_sales_count_final = 0
                        product_price_final = 0
                        brands_ecommerce = BrandsEcommerce.objects.using("ecommerce").get(id=products_ecommerce.brand_id)
                        brand_name_ecommerce = brands_ecommerce.short_name    #need to change it to brandshort name later, coz the model is not yet ready to handle the brand short name
                                      
                        try:
                            brand_store = BrandsStore.objects.get(brand_name__iexact=brand_name_ecommerce)
                            brand_id_store = brand_store.brand_id;
                        except Exception as e:
                            print(f"Exception while fetching the brands from store ==[{brand_name_ecommerce}] == ",e)
                            continue

                        try:
                            size_store = SizesStore.objects.get(size_name__iexact=variant)
                            size_id_store = size_store.size_id
                        except Exception as e:
                            print(f"Exception while fetching the size from store == [{variant}] == ",e)
                            continue

                        try:
                            order_details_ecommerce = OrderDetailsEcommerce.objects.using("ecommerce").filter(product_id=pid,created_at__lt=three_days).exclude(delivery_status__in=exclude_list);
                            # print(f"order details",order_details_ecommerce)
                            if order_details_ecommerce:
                                continue
                        except Exception as e:
                            print(f"Exception while fetching order details from ecommerce == [{pid} - {three_days} - {exclude_list}] == ",e)
                            continue

                        try:
                            products_store = ProductsStore.objects.filter(item_id=item_id_store,size_id=size_id_store,brand_id=brand_id_store,product_expire__gt=twenty_days) #more than one field
                            for p_store in products_store:
                                try:
                                    if p_store.product_price > product_price_final:
                                        product_price_final = p_store.product_price 
                                    product_quantity_final += p_store.product_quantity
                                    sells_store = SellsStore.objects.filter(product_id=p_store.product_id)
                                    if sells_store:
                                        for s_store in sells_store:
                                            product_sales_count_final += s_store.sell_quantity
                                    # else:
                                    #     print(f"sell store is none")
                                except Exception as e:
                                    print(f"Exception while fetching the sell from store ==  [{p_store.product_id}] == ",e)
                            
                            try:
                                resp = ProductStocksEcommerce.objects.using("ecommerce").get(product_id=pid,variant=variant)
                                resp.qty = product_quantity_final - product_sales_count_final
                                # resp.price = product_price_final & product_price_final
                                if product_price_final > 0:
                                    resp.price = product_price_final
                                resp.save()

                            except Exception as e:
                                print(f"Exception while updating product into ecommerce == [{pid} -{variant}] == ",e)

                            print(f" {products_ecommerce.name} {variant} -  {product_quantity_final}, sales {product_sales_count_final}, total = {product_quantity_final-product_sales_count_final}, price is {product_price_final}")

                        except Exception as e:
                            print(f"Exception while fetching the products from store ==  [{item_id_store} - {size_id_store} - {brand_id_store} - {twenty_days}] == ",e)
                        
                    except Exception as e:
                        print(f"Exception while fetching the brands name ==  [{products_ecommerce.brand_id}] == ",e)

                except Exception as e:
                    print(f"Exception while fetching brands is ===  [{pid}] == ",e)

        except Exception as e:
            print(f"1st, stock fetching exception  == ",e)
        
        return Response({
                'success':True,
                'resp':'resp'
            })