from model.recipe import Recipe
from model.source import Source
from model.ingredient import Ingredient

from core.database import(
    SessionLocal,
    engine,
    Base,
    get_db
)

from source.tudogostoso import get_recipe_tudogostoso
import json
import argparse







if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve recipies from TudoGostoso')
    parser.add_argument('--start', action='store', default=1, type=int,
                            required=False, help = 'ID start'
                        )
    parser.add_argument('--end', action='store', default=10, type=int,
                            required=False, help = 'ID end'
                        )
    args = parser.parse_args()
    Base.metadata.create_all(bind=engine)
    id_tudogostoso = Source.find_by_key(session=SessionLocal(), key='TudoGostoso')
    if not id_tudogostoso:
        id_tudogostoso = Source.add(session=SessionLocal(), description='TudoGostoso', key='TudoGostoso')


    for index in range(args.start, args.end):
        print('getting ... {}'.format(index))
        scrap = get_recipe_tudogostoso(index)
        if scrap != False and scrap != 302:
            title = scrap.get('title', '')
            url = scrap.get('original_url', '')
            tempo_preparo = scrap.get('preparation_time', '')
            categoria = scrap.get('category_name', '')
            ingredientes_arr = []
            for ingredient_item in scrap.get('ingredient_lists', [0])[0].get('members', []):
                ingredientes_arr.append(ingredient_item)
            id_recipe = Recipe.add(session=SessionLocal(), description=title, 
                                    source_id=id_tudogostoso.id, url=url,
                                    tempo_preparo=tempo_preparo, categoria=categoria,
                                    ingredientes=json.dumps(ingredientes_arr, ensure_ascii=False).encode('utf-8').decode()
                                )
            for ingredient_item in ingredientes_arr:
                id_item_ingrediente = Ingredient.add(session=SessionLocal(), description=ingredient_item,
                                                        recipe_id=id_recipe.id)
