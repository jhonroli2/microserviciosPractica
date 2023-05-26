
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inventario.models import productos
from django.forms.models import model_to_dict

@csrf_exempt
def productos_view(request):
    
    if request.method == 'GET':
            
            # tomar el id del producto que viene en los query params
            id = request.GET.get('id', None)
            sku = request.GET.get('sku', None)

            # si el id existe, se obtiene el producto de la base de datos
            if id:
                try:
                    producto = productos.objects.get(id=id)
                    return JsonResponse({'producto' : model_to_dict(producto)}, status=200)
                except Exception as e:        
                    return JsonResponse({'error': "Product doesn't exist"}, status=500)
            
            # si el sku existe, se obtiene el producto de la base de datos
            elif sku:
                try:
                    producto = productos.objects.get(sku=sku)
                    return JsonResponse({'producto': model_to_dict(producto)}, status=200)
                except Exception as e:   
                    print(e)     
                    return JsonResponse({'error': "Product doesn't exist"}, status=500)

            else: 
            # Se obtienen todos los productos de la base de datos
                try:
                    producto = productos.objects.all()
                    
                    # Se crea una lista con los productos
                    response = []
                    for p in producto:
                        response.append(p.to_dict_json())
                    
                    # Se retorna la lista de productos en formato JSON
                    return JsonResponse({'productos': response}, status=200)
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=500)


    if request.method == 'POST':
        
        try:
            # Se crea un objeto de tipo productos
            producto = productos()

            request_body = json.loads(request.body)
            
            # Se asignan los valores a los atributos del objeto
            producto.sku = request_body['sku'] if 'sku' in request_body else None
            producto.descripcion = request_body['descripcion'] if 'descripcion' in request_body else None
            producto.referencia = request_body['referencia'] if 'referencia' in request_body else None
            producto.peso = request_body['peso'] if 'peso' in request_body else None
            producto.volumen = request_body['volumen'] if 'volumen' in request_body else None
            producto.costo = request_body['costo'] if 'costo' in request_body else None
            producto.precio = request_body['precio'] if 'precio' in request_body else None
            producto.unidad_empaque = request_body['unidad_empaque'] if 'unidad_empaque' in request_body else None
            producto.proveedor = request_body['proveedor'] if 'proveedor' in request_body else None
            producto.estado = request_body['estado'] if 'estado' in request_body else None

            if producto.sku is None:
                return JsonResponse({'error': 'sku is required'}, status=500)
            if producto.descripcion is None:
                return JsonResponse({'error': 'descripcion is required'}, status=500)
            if producto.referencia is None:
                return JsonResponse({'error': 'referencia is required'}, status=500)
            if producto.peso is None:
                return JsonResponse({'error': 'peso is required'}, status=500)
            if producto.proveedor is None:
                return JsonResponse({'error': 'proveedor is required'}, status=500)
            if producto.unidad_empaque is None:
                return JsonResponse({'error': 'unidad_empaque is required'}, status=500)
            
            producto.save()
            return JsonResponse({'producto': model_to_dict(producto)}, status=200)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    if request.method == 'PUT':

        try:
            # tomar el id del producto que viene en el body
            request_body = json.loads(request.body)

            id = request_body['id'] if 'id' in request_body else None

                
            # si el id existe, se obtiene el producto de la base de datos
            if id:
                try:
                    producto = productos.objects.get(id=id)
                except Exception as e:        
                    return JsonResponse({'error': "Product doesn't exist"}, status=500)
                
                # Se asignan los valores a los atributos del objeto
                producto.sku = request_body['sku'] if 'sku' in request_body else producto.sku
                producto.descripcion = request_body['descripcion'] if 'descripcion' in request_body else producto.descripcion
                producto.referencia = request_body['referencia'] if 'referencia' in request_body else producto.referencia
                producto.peso = request_body['peso'] if 'peso' in request_body else producto.peso
                producto.volumen = request_body['volumen'] if 'volumen' in request_body else producto.volumen
                producto.costo = request_body['costo'] if 'costo' in request_body else producto.costo
                producto.precio = request_body['precio'] if 'precio' in request_body else producto.precio
                producto.unidad_empaque = request_body['unidad_empaque'] if 'unidad_empaque' in request_body else producto.unidad_empaque
                producto.proveedor = request_body['proveedor'] if 'proveedor' in request_body else producto.proveedor
                producto.estado = request_body['estado'] if 'estado' in request_body else producto.estado

                producto.save()
                return JsonResponse({'producto': model_to_dict(producto)}, status=200)
            
            else:
                return JsonResponse({'error': "id is required"}, status=500)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        


