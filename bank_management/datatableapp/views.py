# datatableapp/views.py
from django.shortcuts import render
from django_datatable_view.base_datatable_view import BaseDatatableView
from .models import YourModel


class DataTableView(BaseDatatableView):
    model = YourModel
    columns = ['field1', 'field2', 'field3']  # Replace with actual field names
    order_columns = columns

    def get_initial_queryset(self):
        return YourModel.objects.all()

    def render_column(self, row, column):
        # Customize how each column is rendered
        if column == 'field1':
            return row.field1.upper()
        return super(DataTableView, self).render_column(row, column)
