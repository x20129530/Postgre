from django.db import models
from django.utils.text import slugify
#j Project Table is created
class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    budget = models.IntegerField()
#j Save method is override to generate the new slug automatically
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
#J Function that calulates Budget_left
    def budget_left(self):
        expense_list = Expense.objects.filter(project=self)
        total_expense_amount = 0
        for expense in expense_list:
            total_expense_amount += expense.amount

        return self.budget -total_expense_amount   
#J Function that Calculates Total Transactions
    def total_transactions(self):
        expense_list = Expense.objects.filter(project=self)
        return len(expense_list)
#J Category table is created 
class Category(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
     
#J Expense Table is created
class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8 , decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
#J will order
class Meta:
    ordering = ('-amount',)

