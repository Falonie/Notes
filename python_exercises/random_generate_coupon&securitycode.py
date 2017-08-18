import random, string, logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
print([''.join(i for i in random.choices(string.ascii_letters + string.digits, k=8)) for i in range(10)])
print(random.choice([''.join(i for i in random.choices(string.ascii_letters + string.digits, k=8)) for i in range(200)]))
logging.warning(random.choice([''.join(i for i in random.choices(string.ascii_letters + string.digits, k=8)) for i in range(200)]))
logging.log(level=logging.WARNING, msg=random.choice([''.join(i for i in random.choices(string.ascii_letters + string.digits, k=8)) for i in range(200)]))

print(random.sample(range(1000), k=10))