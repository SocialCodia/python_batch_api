from dbm import dumb
from urllib import response
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import null
from .models import Items as ItemsStore,Products as ProductsStore,Sells as SellsStore,Sizes as SizesStore, Brands as BrandsStore  
from api.ecommerce.models import ProductStocks as ProductStocksEcommerce,OrderDetails as OrderDetailsEcommerce,Products as ProductsEcommerce, Brands as BrandsEcommerce
from datetime import datetime, timedelta


class ProductsView(APIView):
    
    def get(self,request):
        three_days = datetime.now() - timedelta(hours=72)
        twenty_days = datetime.now() - timedelta(hours=480)
        exclude_list = ['cancel','delivered','picked_up','on_the_way']

        try:
            stocks = ProductStocksEcommerce.objects.all().using("ecommerce")
            # print("Stocks  Count Is ",stocks.count())
            for stk in stocks:
                pid = stk.product_id
                variant = stk.variant
                # print(f"Product id is : {pid}, variant is {variant}")
                try:
                    products_ecommerce = ProductsEcommerce.objects.using("ecommerce").get(id=pid)
                    
                    try:
                        product_quantity_final = 0
                        product_sales_count_final = 0
                        product_price_final = 0
                        brands_ecommerce = BrandsEcommerce.objects.using("ecommerce").get(id=products_ecommerce.brand_id)
                        brand_name_ecommerce = brands_ecommerce.name    #need to change it to brandshort name later, coz the model is not yet ready to handle the brand short name
                        
                        try:
                            item_store = ItemsStore.objects.get(pid=pid)
                            item_id_store = item_store.itemid;
                        except Exception as e:
                            print("Exception while fetching the item from store == ",e)
                        
                        try:
                            brand_store = BrandsStore.objects.get(brand_name__iexact=brand_name_ecommerce)
                            brand_id_store = brand_store.brand_id;
                        except Exception as e:
                            print("Exception while fetching the brands from store == ",e)

                        try:
                            size_store = SizesStore.objects.get(size_name__iexact=variant)
                            size_id_store = size_store.size_id
                        except Exception as e:
                            print("Exception while fetching the size from store == ",e)

                        try:
                            order_details_ecommerce = OrderDetailsEcommerce.objects.using("ecommerce").filter(product_id=pid,created_at__lt=three_days).exclude(delivery_status__in=exclude_list);
                            # print("order details",order_details_ecommerce)
                            if order_details_ecommerce:
                                continue
                        except Exception as e:
                            print("Exception while fetching order details from ecommerce == ",e)


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
                                    else:
                                        print("sell store is none")
                                except Exception as e:
                                    print("Exception while fetching the sell from store == ",e)
                            
                            try:
                                resp = ProductStocksEcommerce.objects.using("ecommerce").get(product_id=pid,variant=variant)
                                resp.qty = product_quantity_final - product_sales_count_final
                                # resp.price = product_price_final & product_price_final
                                if product_price_final > 0:
                                    resp.price = product_price_final
                                resp.save()

                            except Exception as e:
                                print("Exception while updating product into ecommerce",e)

                            print(f"{item_store.itemname} - {variant} -  {product_quantity_final}, sales {product_sales_count_final}, total = {product_quantity_final-product_sales_count_final}, price is {product_price_final}")

                        except Exception as e:
                            print("Exception while fetching the products from store == ",e)
                        


                    except Exception as e:
                        print("Exception while fetching the brands name == ",e)

                except Exception as e:
                    print("Exception while fetching brands is === ",e)

        except Exception as e:
            print("1st, stock fetching exception",e)
        
        return Response({
                'success':True
            })
    
    def gets(self,request):
        three_days = datetime.now() - timedelta(hours=72)
        exclude_list = ['cancel','delivered','picked_up','on_the_way']
        try:
            stocks = ProductStocksEcommerce.objects.all().using('ecommerce');                                # fetching stock from ecommerce
            # print('============ stock is : ============',stocks)
            for stk in stocks:
                pid = stk.product_id
                input_size = stk.variant
                try:
                    sell_count = 0
                    product_quantity = 0
                    largest_price = 0
                    item = ItemsStore.objects.get(pid=pid)                                               # fetching items from management
                    # print('============ item is : ============',item)
                    size = SizesStore.objects.get(size_name__iexact=input_size)                          # fetching size from management
                    # print('============ size is : ============',size)
                    product = ProductsStore.objects.filter(item_id=item.itemid,size_id=size.size_id);    # fetching product from management
                    # print('============ product is : ============',product)
                    
                    for p in product:
                        try:
                            order_details = OrderDetailsEcommerce.objects.filter(product_id=pid,created_at__gt=three_days,variation__iexact=input_size).using('ecommerce').exclude(delivery_status__in=exclude_list);
                            print(f'============ order_details is : pid = {pid} , size = {input_size}, count = {order_details.count()}',)
                            # print("order_details query is : ",order_details.query)
                            if order_details.count() > 0:
                                continue
                        except Exception as e:
                            print("Exception is : ",e)
                            continue
                        if p.product_price > largest_price:
                            largest_price = p.product_price
                        try:
                            sales = SellsStore.objects.filter(product_id=p.product_id)
                            # print('============ sales is : ============',sales)
                            print('============ sales is1 : ============',sales.count(),p.product_quantity)
                            if (sales.count()<1):
                                product_quantity = p.product_quantity
                                continue
                            for s in sales:
                                sell_count += s.sell_quantity
                                product_quantity += p.product_quantity
                        except Exception as e:
                            print("Exception is : ",e)
                            continue

                    quantity = product_quantity - sell_count

                    # print("product quantitiy is",quantity)
                    # print("product largest_price is",largest_price)

                    try:
                        resp = ProductStocksEcommerce.objects.using('ecommerce').get(pk=stk.id)
                        # print('============ resp is : ============',resp)
                        print('----------------',product_quantity);
                        resp.qty=product_quantity
                        resp.price=largest_price
                        if largest_price > 0 :
                            resp.save()
                    except Exception as e:
                        print("Exception is : ",e)
                        continue
                except Exception as e:
                    print("Exception is : ",e)
                    continue

            return Response({
                'success':True,
                'message':'Batch Executed Successfully'
            })
        except Exception as e:
            print("Exception is : ",e)
            return Response({
                'success':True,
                'message':'Batch Execution Failed',
                'error':str(e)
            })
