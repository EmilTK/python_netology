def cook_book():
    recipes_book = {}
    with open('files/recipes.txt', encoding='utf-8') as file:
        dish = ''
        for row in file:
            if (len(row.strip()) > 1) and ('|' not in row.strip()):
                dish = row.strip()
                recipes_book[row.strip()] = []
            elif '|' in row.strip():
                ingredient = row.strip().replace(' ', '').split('|')
                recipes_book[dish].append({'ingredient_name': ingredient[0],
                                        'quantity': int(ingredient[1]),
                                        'measure': ingredient[2]})
    return recipes_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_need = {}
    for dish in dishes:
        for ingredient in cook_book()[dish]:
            if ingredients_need.get(ingredient['ingredient_name']) is None:
                ingredients_need[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                   'quantity': ingredient['quantity']*person_count}
            else:
                ingredients_need[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
    return ingredients_need




def task_3():
    files_list = {'1.txt', '2.txt', '3.txt'}
    max_row = []
    for file in files_list:
        with open(f'files/{file}', encoding='utf-8') as f:
            rows = f.readlines()
            max_row.append([len(rows), file])

    for file in sorted(max_row):
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(file[1] + '\n')
            f.write(str(file[0]) + '\n')
            with open(f'files/{file[1]}', encoding='utf-8') as f2:
                f.write(f2.read()+'\n')


def main():
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    task_3()


if __name__=='__main__':
    main()