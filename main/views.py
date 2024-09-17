from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ShopEntryForm
from main.models import ShopEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    shop_entries = ShopEntry.objects.all()
    
    context = {
        # 'product_name': 'Sofa Ruang Tamu',
        # 'product_price': 'IDR 1,500,000',
        # 'product_description': 'A sofa-bed with small, neat dimensions which is easy to furnish with, even when space is limited. You can make the sofa more comfortable and personal by completing with pillows in different colours and patterns.',
        # 'stock': 1,
        # 'product_location': 'Jakarta, Surabaya, Bali',
        'name' : "Gnade Yuka",
        'kelas' : "PBP-B",
        'shop_entries' : shop_entries
    }

    return render(request, "main.html", context)

def create_shop_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shop_entry.html", context)

def show_xml(request):
    data = ShopEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ShopEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ShopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ShopEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
