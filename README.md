# BasicKafkaCDCProject

Basit bir Kafka CDC Projesi

## Projenin Tanımı

- Kafka broker'ı ve ZooKeeper'ı çalıştıran Docker Compose dosyası sağlar.
- "a_app" ve "b_app" adında iki örnek mikro hizmet içerir, her biri Kafka ile etkileşimde bulunur.
- "a_app" yeni belgeleri MongoDB'den alır ve Kafka'ya gönderir.
- "b_app" Kafka'dan gelen mesajları alır ve işler.

## Kullanılan Teknolojiler

- Docker
- Apache Kafka
- ZooKeeper
- MongoDB

## Kurulum

Uygulamaları oluşturmak ve çalıştırmak için şu adımları izleyin:

1. İlk olarak projeyi kopyalayın:

   ```bash
   git clone https://github.com/zeynepkocc/BasicKafkaCDCProject.git
   ```

2. Daha sonra projenin olduğu dizine gidin:

    ```bash
    cd BasicKafkaCDCProject
    ```

3. Projeyi çalıştırın:

   ```bash
   docker compose up --build
   ```

4. Veri akışını sağlamak için terminal hala uygulama dosyasında iken aşağıdaki komutu girin:

    ```bash
    python kafka-producer.py
    ```

5. Bu adımlardan sonra veri akışı terminalde ve veritabanında gözlemlenecektir.


## Lisans

[MIT License](LICENSE).
