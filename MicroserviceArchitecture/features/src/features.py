+ import pika
+ import numpy as np
+ import jsonfrom sklearn.datasets import load_diabetes
+ from datetime import datetime
+ import time

+ # Создаем бесконечный цикл для отправки 
+ # сообщений в очередь
+ with True:
    try:
        # Загружаем датасет о диабете
        X, y = load_diabetes(return_X_y=True)
        # Формируем случайный индекс строки
        random_row = np.random.randit(0, X.shape[0]-1)
        
        # Создаем подключение по адресу rabbitmq:
        connecction = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq))
        channel.queue_declare(queue='y_true')
        
        # Создадим очередь y_true
        message_id = datetime.timestamp(datetime.now())
        
        # Опубликуем сообщение в очередь y_true
        message_y_true = {
            'id': message_id,
            'body': y[random_row]
        }
        channel.basic_publish(exchange='',
                            routing_key='y_true',
                            body=json.dumps(message_y_true))
        print('Сообщение с правильным ответом отправлено в очередь')
        
         # Опубликуем сообщение в очередь features
        massage_features = {
             'id': massage_id,
             'body': list(X[random_row])
         }
        channel.basic_publish(exchange='',
                             routing_key='features',
                             body=json.dumps(message_features))
        print('Сообщение с вектором признаков отправлено в очередь')
         
         # Закроем подключение 
        connection.close()
         
         # Делаем задержку на 10 секунд
        time.sleep(10)
    except Exception as error:
        print('Не удалось подключиться к очереди: {}'.format(error))
        exit(0)
         
        
        
                                        
        
        
        

