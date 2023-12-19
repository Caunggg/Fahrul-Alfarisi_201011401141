import sys
from colorama import Fore, Style
from models import Base, Smartphone
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import DEV_SCALE_brand,DEV_SCALE_ram,DEV_SCALE_processor,DEV_SCALE_rom,DEV_SCALE_baterai,DEV_SCALE_harga

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-5
        self.raw_weight = {'brand': 4, 'ram': 3, 'processor': 4, 'rom': 3, 'baterai': 3, 'harga': 2}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k,v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphone)
        return [{'id': smartphonesamsung.id, 'brand': DEV_SCALE_brand[smartphonesamsung.brand], 'ram': DEV_SCALE_ram[smartphonesamsung.ram], 'processor': DEV_SCALE_processor[smartphonesamsung.processor], 'rom': DEV_SCALE_rom[smartphonesamsung.rom], 'baterai': DEV_SCALE_baterai[smartphonesamsung.baterai], 'harga': DEV_SCALE_harga[smartphonesamsung.harga]} for smartphonesamsung in session.scalars(query)]
    
    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brands = [] # max
        rams = [] # max
        processors = [] # max
        roms = [] # max
        baterais = [] # max
        hargas = [] # min
        for data in self.data:
            brands.append(data['brand'])
            rams.append(data['ram'])
            processors.append(data['processor'])
            roms.append(data['rom'])
            baterais.append(data['baterai'])
            hargas.append(data['harga'])
        max_brand = max(brands)
        max_ram = max(rams)
        max_processor = max(processors)
        max_rom = max(roms)
        max_baterai = max(baterais)
        min_harga = min(hargas)
        return [
            {   'id': data['id'],
                'brand': data['brand']/max_brand, # benefit
                'ram': data['ram']/max_ram, # benefit
                'processor': data['processor']/max_processor, # benefit
                'rom': data['rom']/max_rom, # benefit
                'baterai': data['baterai']/max_baterai, # benefit
                'harga': min_harga/data['harga'] # cost
                }
            for data in self.data
        ]

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result =  {row['id']:
            round(
                row['brand']**weight['brand'] *
                row['ram']**weight['ram'] *
                row['processor']**weight['processor'] *
                row['rom']**weight['rom'] *
                row['baterai']**weight['baterai'] *
                row['harga']**weight['harga'], 
                2)
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['id']:
            round(row['brand'] * weight['brand'] +
            row['ram'] * weight['ram'] +
            row['processor'] * weight['processor'] +
            row['rom'] * weight['rom'] +
            row['baterai'] * weight['baterai'] +
            row['harga'] * weight['harga'], 2)
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)
    

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)
    pass

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
