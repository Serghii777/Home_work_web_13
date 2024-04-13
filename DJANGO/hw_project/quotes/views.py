from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Tag
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count



def main(request, page=1):
    quotes = Quote.objects.all().order_by('id')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    return render(request, "quotes/index.html", context={"quotes": quotes_on_page, "quote": quotes})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user  
            author.save()
            return redirect(to='quotes:root')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.author = Author.objects.get(user=request.user)  
            quote.save()
            form.save_m2m()  
            return redirect(to='quotes:root') 
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})

def quotes_by_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    quotes = tag.quote_set.all()
    return render(request, 'quotes/quotes_by_tag.html', {'tag': tag, 'quotes': quotes})

def top_ten_tags(request):
    top_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    return render(request, 'quotes/top_ten_tags.html', {'top_tags': top_tags})