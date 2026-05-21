first_name = "Lebron"
last_name = "Shaq"


if len(first_name) > len(last_name):
    x=(len(first_name)-len(last_name))
    if x==1:
              print(first_name,"is longer than",last_name,"by 1 letter")
    elif x > 1:
              print(first_name,"is longer than",last_name,"by",x,"letters")

elif len(first_name) < len(last_name):

    x=(len(last_name)-len(first_name))
    if x==1:
              print(last_name,"is longer than",first_name,"by 1 letter")
    elif x > 1:
              print(last_name,"is longer than",first_name,"by",x,"letters")

else:

    print(first_name,"and",last_name,"are the same length")
