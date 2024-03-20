# CREATE TABLE `products` (
#   `ProductId` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
#   `Name` varchar(255) NOT NULL,
#   `Status` int DEFAULT NULL,
#   `Stock` int DEFAULT NULL,
#   `Description` text,
#   `Price` float DEFAULT NULL,
#   `Discount` int DEFAULT NULL,
#   `FinalPrice` float DEFAULT NULL,
#   `UpdatedAt` datetime DEFAULT NULL,
#   `CreatedAt` datetime DEFAULT NULL,
#   PRIMARY KEY (`ProductId`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;