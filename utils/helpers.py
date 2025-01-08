from rest_framework.pagination import PageNumberPagination
from collections import defaultdict
from decimal import Decimal
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

def paginate_response(queryset, request, serializer_class):
    paginator = CustomPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = serializer_class(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)

def calculate_settlement_suggestions(group):
    """Calculates settlement suggestions for a group."""
    balances = defaultdict(Decimal)
    expenses = group.expense_set.all()
    settlements = group.settlement_set.all()
    for expense in expenses:
      participants_count = len(expense.participants.all())
      amount_per_participant = expense.amount/Decimal(participants_count)
      for participant in expense.participants.all():
          balances[participant] -= amount_per_participant
      balances[expense.created_by] += expense.amount
    for settlement in settlements:
      balances[settlement.payer] -= settlement.amount
      balances[settlement.payee] += settlement.amount

    positive_balances = []
    negative_balances = []
    for user, balance in balances.items():
        if balance > 0:
           positive_balances.append((user, balance))
        elif balance < 0:
            negative_balances.append((user, abs(balance)))
    settlement_suggestions = []
    i = 0
    j = 0
    while i < len(negative_balances) and j < len(positive_balances):
        debtor, debt_amount = negative_balances[i]
        creditor, credit_amount = positive_balances[j]
        settlement_amount = min(debt_amount, credit_amount)
        settlement_suggestions.append({
            'from': debtor.id,
            'to': creditor.id,
            'amount': float(settlement_amount)
        })
        negative_balances[i] = (debtor, debt_amount-settlement_amount)
        positive_balances[j] = (creditor, credit_amount-settlement_amount)
        if negative_balances[i][1] == 0: i +=1
        if positive_balances[j][1] == 0: j +=1
    return settlement_suggestions