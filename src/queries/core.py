from sqlalchemy import text
from database import sync_engine, async_engine
from models import metadata_obj

# sync проверка 
def get_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')

# async проверка 
async def get_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')

def create_tables():
    metadata_obj.drop_all(sync_engine)    
    metadata_obj.create_all(sync_engine)