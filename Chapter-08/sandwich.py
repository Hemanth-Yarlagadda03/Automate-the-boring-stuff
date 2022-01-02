import pyinputplus as pyp
import random





prices = {'wheat': 25, 'white': 20, 'sour dough': 30, 'chicken': 150, 'turkey': 300, 'ham': 500, 'tofu': 150,
          'cheddar': 30, 'swiss': 25, 'mozzarella': 15, 'mayo': 10, 'mustard': 10, 'lettuce': 20,
          'ketchup': 5}

while True:
    items = []
    items.append(pyp.inputMenu(['wheat', 'white', 'sour dough'],
                          prompt='Please select the type of bread you want for your sandwich: \n',
                          numbered=True))

    items.append(pyp.inputMenu(['chicken', 'turkey', 'Ham', 'tofu'],
                            prompt='Which type of protein you would like: \n',
                            numbered=True))

    if pyp.inputYesNo('Do you want Cheese in your sandwich?(Y/N)\n')== 'yes':
        items.append(pyp.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True))

    if pyp.inputYesNo('Do you want mayo?(Y/N) \n') == 'yes':
        items.append('mayo')
    if pyp.inputYesNo('Do you want mustard?(Y/N) \n') == 'yes':
        items.append('mustard')
    if pyp.inputYesNo('Do you want lettuce?(Y/N) \n') == 'yes':
        items.append('lettuce')
    if pyp.inputYesNo('Do you want tomato ketchup?(Y/N) \n') == 'yes':
        items.append('ketchup')

    sandwichno = pyp.inputInt('How much sandwiches you would like to order?\n',
                              blockRegexes=['[0|-|.]'])

    sum = 0
    print(f'Your sandwich ingredients and prices are as follows: \n')
    for item in items:
        price = prices[item]
        print(f'{item}= {price}')
        sum += price

    print(f"sandwich cost x number of sandewiches ordered = {sum}x{sandwichno} = {sum}*{sandwichno}")

    
    if pyp.inputYesNo('Please confirm your order: (Y/N)\n')== 'yes':
        print('Please take your order number from the machine and you will be notified when '
              'your order is ready\n' 'Your order number is' ,(random.randint(0,100)))
        
              
        break