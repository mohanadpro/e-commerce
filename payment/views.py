from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import CardSerializer
import stripe
import os
SECRET_KEY = os.environ.get('S_SECRET_KEY')

stripe.api_key=SECRET_KEY

def generate_card_token(card_number,exp_month,exp_year,cvv):
    data= stripe.Token.create(
            card={
                "number": str(card_number),
                "exp_month": int(exp_month),
                "exp_year": int(exp_year),
                "cvc": str(cvv),
            })
    card_token = data['id']
    return card_token


def create_payment_charge(tokenid, amount):
    payment = stripe.Charge.create(
                amount= int(amount)*100,                  # convert amount to cents
                currency='usd',
                description='Example charge',
                source=tokenid,
                )

    payment_check = payment['paid']    # return True for successfull payment
    return payment_check



class Payment(generics.ListCreateAPIView):
    serializer_class = CardSerializer
    def post(self, request):
        try:
            card_number = request.POST.get('card_number')
            exp_month = request.POST.get('exp_month')
            exp_year = request.POST.get('exp_year')
            cvv = request.POST.get('cvv')
            amount = float(request.POST.get('amount'))
            token_id = generate_card_token(card_number, exp_month, exp_year, cvv)
            is_paid_done = create_payment_charge(token_id, amount)
            data = {'message': 'Payment has been done successfully... '}
            return Response(data, status=200)
        except Exception as e:
            print(e)
            data = {'message': 'Payment has been done successfully... '}
            return Response(data, status=400)

