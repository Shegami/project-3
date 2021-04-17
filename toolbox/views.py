from django.shortcuts import render, redirect, HttpResponse
from toolbox.forms import NewClientForm, NewProjectForm, NewInvoiceForm, NewActForm
from toolbox.models import Act, Invoice, Client, Project


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')


def mr_redirect(request, model_id=None, model_name=None):
    button = request.POST['button']
    if button == 'create_client':
        return redirect('create_client')
    elif button == 'create_project':
        return redirect('create_project')
    elif button == 'create_invoice':
        return redirect('create_invoice')
    elif button == 'create_act':
        return redirect('create_act')
    elif 'get' in button:
        return redirect('get_model', button)


def get_model(request, button):
    if 'acts' in button:
        context = {'models': Act.objects.all().order_by('id')}
        return render(request, 'get_acts.html', context)
    elif 'invoices' in button:
        context = {'models': Invoice.objects.all().order_by('id')}
        return render(request, 'get_invoices.html', context)
    elif 'clients' in button:
        context = {'models': Client.objects.all().order_by('id')}
        return render(request, 'get_clients.html', context)
    else:
        context = {'models': Project.objects.all().order_by('id')}
        return render(request, 'get_projects.html', context)


def create_client(request):
    return create_form(request, NewClientForm(), 'creation.html')


def create_project(request):
    return create_form(request, NewProjectForm(), 'creation.html')


def create_invoice(request):
    return create_form(request, NewInvoiceForm(), 'creation.html')


def create_act(request):
    return create_form(request, NewActForm(), 'creation.html')


def create_form(request, form, link):
    if request.method == 'GET':
        context = {
            'form': form
        }
        return render(request, link, context)
    else:
        form = form(request.POST)
        if form.is_valid():
            if form == NewInvoiceForm():
                pre_form = form.save(commit=False)
                pre_form.client = pre_form.project.client
                pre_form.save()
            elif form == NewActForm():
                pre_form = form.save(commit=False)
                pre_form.client = pre_form.invoice.client
                pre_form.project = pre_form.invoice.project
                pre_form.amount = pre_form.invoice.amount
                pre_form.currency = pre_form.invoice.currency
                pre_form.save()
            form.save()
            return redirect(link)
        errors = form.errors
        return HttpResponse(f'error in {errors}')


def mr_editor(request, model_id, model_name, link):
    button = request.POST['button']
    if button == 'edit':
        if model_name == 'Client':
            return redirect('edit_client', model_id)
        elif model_name == 'Project':
            return redirect('edit_project', model_id)
        elif model_name == 'Act':
            return redirect('edit_act', model_id)
        elif model_name == 'Invoice':
            return redirect('edit_invoice', model_id)
    elif button == 'delete':
        return redirect('delete_model', model_name, model_id, link)


def edit_client(request, model_id):
    return edit_model(request, NewClientForm(), 'edition.html', Client, model_id)


def edit_act(request, model_id):
    return edit_model(request, NewActForm(), 'edition.html', Act, model_id)


def edit_invoice(request, model_id):
    return edit_model(request, NewInvoiceForm(), 'edition.html', Invoice, model_id)


def edit_project(request, model_id):
    return edit_model(request, NewProjectForm(), 'edition.html', Project, model_id)


def edit_model(request, form, link, model_type, model_id):
    if request.method == 'GET':
        context = {
            'form': form,
            'model_id': model_id
        }
        return render(request, link, context)
    model = model_type.objects.get(pk=model_id)
    edited_model = form(request.POST, instance=model)
    edited_model.save()
    return redirect('main')


def delete_model(request, model_name, model_id, link):
    if model_name == 'Act':
        model = Act.objects.get(pk=model_id)
    elif model_name == 'Invoice':
        model = Invoice.objects.get(pk=model_id)
    elif model_name == 'Project':
        model = Project.objects.get(pk=model_id)
    elif model_name == 'Client':
        model = Client.objects.get(pk=model_id)
    model.delete()
    return redirect('get_model', link)
