from django.db.backends.mysql.base import DatabaseWrapper as MySQLDatabaseWrapper

from .features import DatabaseFeatures


class DatabaseWrapper(MySQLDatabaseWrapper):
    features_class = DatabaseFeatures

    def check_database_version_supported(self) -> None:
        if self.mysql_is_mariadb:
            # MariaDB 10.4 é plenamente capaz de atender às necessidades deste projeto.
            if self.mysql_version < (10, 4, 0):
                super().check_database_version_supported()
            return

        super().check_database_version_supported()
