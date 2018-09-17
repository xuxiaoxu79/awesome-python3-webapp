import logging
import orm
import asyncio
from models import User
logging.basicConfig(
    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO
)


async def test(loop):
    await orm.create_pool(loop, user='user', password='password', db='mydb')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    await u.save()


async def find(loop):
    await orm.create_pool(loop, user='user', password='password', db='mydb')
    rs = await User.findAll()
    print('查找测试： %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test(loop), find(loop)]))
loop.run_forever()
