import uuid
import _thread
from google.cloud.spanner import Client, TransactionPingingPool

def run_writes(database):
    while 1:
        id = str(uuid.uuid4())
        with database.batch() as batch:
            batch.insert(
                table='Albums',
                columns=("AlbumId", 'Year', 'AlbumTitle'),
                values=[(id, 2021, "AlbumTitle"),]
                )

if __name__ == "__main__":
    try:
        client = Client()
        instance = client.instance('codelab-instance')
        pool = TransactionPingingPool(size=10, default_timeout=5, ping_interval=300)
        database = instance.database('codelabdb')
        for _ in range(10):
            _thread.start_new_thread(run_writes,(database,))
            print('started Thread' + str(_))
    except:
        print('Unable to start new thread')
    while 1:
        pass