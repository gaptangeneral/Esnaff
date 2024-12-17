from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import GelirGider, AlacakVerecek, CekSenet, Fis, Fatura, Veresiye, Kategori
from .forms import KategoriForm, GelirGiderForm, AlacakVerecekForm, CekSenetForm, FisForm, FaturaForm, VeresiyeForm

# Kategori Görünümleri
class KategoriListView(ListView):
    model = Kategori
    template_name = 'finance/kategori/kategori_list.html'
    context_object_name = 'kategori_list'

class KategoriCreateView(CreateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'finance/kategori/kategori_form.html'
    success_url = reverse_lazy('kategori_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Kategori başarıyla oluşturuldu.")
        return super().form_valid(form)

class KategoriUpdateView(UpdateView):
    model = Kategori
    form_class = KategoriForm
    template_name = 'finance/kategori/kategori_form.html'
    success_url = reverse_lazy('kategori_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Kategori başarıyla güncellendi.")
        return super().form_valid(form)

class KategoriDeleteView(DeleteView):
    model = Kategori
    template_name = 'finance/kategori/kategori_confirm_delete.html'
    success_url = reverse_lazy('kategori_listesi')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, f"{obj.ad} kategorisi başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Gelir Gider Görünümleri
class GelirGiderListView(ListView):
    model = GelirGider
    template_name = 'finance/gelir_gider/gelir_gider_list.html'
    context_object_name = 'gelir_gider_list'

class GelirGiderCreateView(CreateView):
    model = GelirGider
    form_class = GelirGiderForm
    template_name = 'finance/gelir_gider/gelir_gider_form.html'
    success_url = reverse_lazy('gelir_gider_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Gelir/Gider başarıyla kaydedildi.")
        return super().form_valid(form)

class GelirGiderUpdateView(UpdateView):
    model = GelirGider
    form_class = GelirGiderForm
    template_name = 'finance/gelir_gider/gelir_gider_form.html'
    success_url = reverse_lazy('gelir_gider_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Gelir/Gider başarıyla güncellendi.")
        return super().form_valid(form)

class GelirGiderDeleteView(DeleteView):
    model = GelirGider
    template_name = 'finance/gelir_gider/gelir_gider_confirm_delete.html'
    success_url = reverse_lazy('gelir_gider_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Gelir/Gider başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Alacak Verecek Görünümleri
class AlacakVerecekListView(ListView):
    model = AlacakVerecek
    template_name = 'finance/alacak_verecek/alacak_verecek_list.html'
    context_object_name = 'alacak_verecek_list'

class AlacakVerecekCreateView(CreateView):
    model = AlacakVerecek
    form_class = AlacakVerecekForm
    template_name = 'finance/alacak_verecek/alacak_verecek_form.html'
    success_url = reverse_lazy('alacak_verecek_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Alacak/Verecek başarıyla kaydedildi.")
        return super().form_valid(form)

class AlacakVerecekUpdateView(UpdateView):
    model = AlacakVerecek
    form_class = AlacakVerecekForm
    template_name = 'finance/alacak_verecek/alacak_verecek_form.html'
    success_url = reverse_lazy('alacak_verecek_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Alacak/Verecek başarıyla güncellendi.")
        return super().form_valid(form)

class AlacakVerecekDeleteView(DeleteView):
    model = AlacakVerecek
    template_name = 'finance/alacak_verecek/alacak_verecek_confirm_delete.html'
    success_url = reverse_lazy('alacak_verecek_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Alacak/Verecek başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Çek Senet Görünümleri
class CekSenetListView(ListView):
    model = CekSenet
    template_name = 'finance/cek_senet/cek_senet_list.html'
    context_object_name = 'cek_senet_list'

class CekSenetCreateView(CreateView):
    model = CekSenet
    form_class = CekSenetForm
    template_name = 'finance/cek_senet/cek_senet_form.html'
    success_url = reverse_lazy('cek_senet_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Çek/Senet başarıyla kaydedildi.")
        return super().form_valid(form)

class CekSenetUpdateView(UpdateView):
    model = CekSenet
    form_class = CekSenetForm
    template_name = 'finance/cek_senet/cek_senet_form.html'
    success_url = reverse_lazy('cek_senet_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Çek/Senet başarıyla güncellendi.")
        return super().form_valid(form)

class CekSenetDeleteView(DeleteView):
    model = CekSenet
    template_name = 'finance/cek_senet/cek_senet_confirm_delete.html'
    success_url = reverse_lazy('cek_senet_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Çek/Senet başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Fiş Görünümleri
class FisListView(ListView):
    model = Fis
    template_name = 'finance/fis/fis_list.html'
    context_object_name = 'fis_list'

class FisCreateView(CreateView):
    model = Fis
    form_class = FisForm
    template_name = 'finance/fis/fis_form.html'
    success_url = reverse_lazy('fis_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Fiş başarıyla kaydedildi.")
        return super().form_valid(form)

class FisUpdateView(UpdateView):
    model = Fis
    form_class = FisForm
    template_name = 'finance/fis/fis_form.html'
    success_url = reverse_lazy('fis_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Fiş başarıyla güncellendi.")
        return super().form_valid(form)

class FisDeleteView(DeleteView):
    model = Fis
    template_name = 'finance/fis/fis_confirm_delete.html'
    success_url = reverse_lazy('fis_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Fiş başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Fatura Görünümleri
class FaturaListView(ListView):
    model = Fatura
    template_name = 'finance/fatura/fatura_list.html'
    context_object_name = 'fatura_list'

class FaturaCreateView(CreateView):
    model = Fatura
    form_class = FaturaForm
    template_name = 'finance/fatura/fatura_form.html'
    success_url = reverse_lazy('fatura_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Fatura başarıyla kaydedildi.")
        return super().form_valid(form)

class FaturaDetailView(DetailView):
    model = Fatura
    template_name = 'finance/fatura/fatura_detail.html'
    context_object_name = 'fatura'

class FaturaUpdateView(UpdateView):
    model = Fatura
    form_class = FaturaForm
    template_name = 'finance/fatura/fatura_form.html'
    success_url = reverse_lazy('fatura_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Fatura başarıyla güncellendi.")
        return super().form_valid(form)

class FaturaDeleteView(DeleteView):
    model = Fatura
    template_name = 'finance/fatura/fatura_confirm_delete.html'
    success_url = reverse_lazy('fatura_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Fatura başarıyla silindi.")
        return super().delete(request, *args, **kwargs)

# Veresiye Görünümleri
class VeresiyeListView(ListView):
    model = Veresiye
    template_name = 'finance/veresiye/veresiye_list.html'
    context_object_name = 'veresiye_list'

class VeresiyeCreateView(CreateView):
    model = Veresiye
    form_class = VeresiyeForm
    template_name = 'finance/veresiye/veresiye_form.html'
    success_url = reverse_lazy('veresiye_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Veresiye başarıyla kaydedildi.")
        return super().form_valid(form)

class VeresiyeUpdateView(UpdateView):
    model = Veresiye
    form_class = VeresiyeForm
    template_name = 'finance/veresiye/veresiye_form.html'
    success_url = reverse_lazy('veresiye_listesi')

    def form_valid(self, form):
        messages.success(self.request, "Veresiye başarıyla güncellendi.")
        return super().form_valid(form)

class VeresiyeDeleteView(DeleteView):
    model = Veresiye
    template_name = 'finance/veresiye/veresiye_confirm_delete.html'
    success_url = reverse_lazy('veresiye_listesi')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Veresiye başarıyla silindi.")
        return super().delete(request, *args, **kwargs)