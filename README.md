# Web_BI_Store_Skynet
Repositorio de Proyecto de Catedra, Proceso 01-2024

Para desplegar la instancia primero que nada debemos instalar las dependencias de libererias en este caso para el ambiente local se recomienda usar un virtual enviroment para instalar las libreria contamos con el archivo de requirements.txt, usaremos el comando 

pip install -r requirements.txt

Una ves tenemos instaladas las dependencias podremos desplegar el proyecto con el comando de 

flask run 

DDL para la tables

Tabla base de usuarios para el sistema

CREATE TABLE `tmp_jr_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `created_by` bigint NOT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tmp_jr_user_unique` (`username`),
  UNIQUE KEY `tmp_jr_user_unique_1` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

Tabla de proyecciones como header

CREATE TABLE `tmp_jr_proyection` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `created_by` bigint NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date_from` datetime DEFAULT NULL,
  `date_to` datetime DEFAULT NULL,
  `days_to_project` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

Tabla de Inventarios

CREATE TABLE `tmp_jr_inventory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_qty` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sale_date` datetime DEFAULT NULL,
  `id_projection` bigint DEFAULT NULL,
  `branch` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_ml_generated` tinyint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;