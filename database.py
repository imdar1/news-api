  
import mysql.connector
from secret import Secret
from model.response import Response


class DatabaseResponse(Response):
    def __init__(self, data, message, status):
        super().__init__(data=data,
                         message=message,
                         status=status)

class Database:
    READ = 0
    WRITE = 1

    def _open_connection(self):
        if Secret.HOST == "":
            self.connection = mysql.connector.connect(unix_socket=Secret.UNIX_SOCKET,
                                                user=Secret.USER,
                                                passwd=Secret.PASSWORD,
                                                database=Secret.DB)
        else:
            self.connection = mysql.connector.connect(host=Secret.HOST,
                                                user=Secret.USER,
                                                passwd=Secret.PASSWORD,
                                                database=Secret.DB)
        self.cursor = self.connection.cursor()
    
    def __init__(self):
        self._open_connection()

    def execute(self, operation, query, param=None):
        try:
            if operation == Database.READ:
                if param is None:
                   self.cursor.execute(query)
                else:
                   self.cursor.execute(query, param)
                return DatabaseResponse(data=self.cursor.fetchall(),
                                        message="",
                                        status=True)

            elif operation == Database.WRITE:
                self.cursor.execute(query, param)
                connection.commit()
                return DatabaseResponse(data=[],
                                        message="",
                                        status=True)
        except Exception as e:
            return DatabaseResponse(data=[],
                                    message=str(e),
                                    status=False)
    
    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
