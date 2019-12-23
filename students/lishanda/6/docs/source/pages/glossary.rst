############
Glossary
############


.. glossary::
   Ingredient
      title

   Pizza
      title, price, ingredients: [:term:`Ingredient`]

   Order
      order_date, pizzas: [:term:`Pizza`], delivery_address, customer_email, email_sent,
      status (enum: 'ACCEPTED', 'COOKING', 'DELIVERY', 'FINISHED')
