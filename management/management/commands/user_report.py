from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from management.models import User
from management.models_list.order import Order
from django.db.models import Sum, F, Min, Max, Avg
from django.db import connection


class Command(BaseCommand):
    help = 'Displays Report'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--user', nargs='+', type=str, help='User ID')

    def handle(self, *args, **kwargs):
        # userId = kwargs['user']

        # order = Order.objects.filter(user__role__name='user',user__in=userId) if userId else Order.objects.filter(user__role__name='user')
        # total_spendings_orders = order.values('id','user').annotate(
        #     total=Sum(F('ordereditems__item__price') * F('ordereditems__quantity'))
        # )

        # result = {}
        # users = User.objects.filter(role__name='user',id__in=userId) if userId else User.objects.filter(role__name='user')
        # for user in users:
        #     filter = total_spendings_orders.filter(user=user)
        #     min_total = filter.aggregate(Min('total'))['total__min']
        #     max_total = filter.aggregate(Max('total'))['total__max']
        #     avg_total = filter.aggregate(Avg('total'))['total__avg']
        #     total = filter.aggregate(Sum('total'))['total__sum']

        #     result[user.username] = {'Minimum per order':min_total, 'Maximum per order' : max_total, 'Average' : avg_total, 'Total' : total}

        # df = pd.DataFrame(result)
        # print(df)

        


        cursor = connection.cursor()

        menu = cursor.execute('''SELECT * from management_menu''').fetchall()
        menuResult = [{cursor.description[index][0]:column for index, column in enumerate(value)} for value in menu]
        menuDF = pd.DataFrame(menuResult)
        functions = {
            'average': menuDF["price"].mean(),
            'minimum': menuDF["price"].min(),
            'maximum': menuDF["price"].max(),
            'total': menuDF["price"].sum(),
            'count': menuDF["price"].count(),
        }
        menuResultsDF = pd.DataFrame(functions, index=[0])

        menuQuery = cursor.execute('''SELECT AVG(price) as average, MIN(price) as minimum, MAX(price) as maximum, SUM(price) as total, COUNT(price) as count from management_menu''').fetchall()
        menuQueryResult = [{cursor.description[index][0]:column for index, column in enumerate(value)} for value in menuQuery]
        menuQueryDF = pd.DataFrame(menuQueryResult)

        result = pd.concat([menuResultsDF,menuQueryDF])
        print(result)
        print(menuResultsDF.equals(menuQueryDF))

