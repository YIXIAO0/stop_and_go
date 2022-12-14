import obd

class OBD:
    def __init__(self):
        self.connection = obd.OBD(portstr='/dev/tty.usbserial-1130')
        if not self.connection.is_connected():
            print("obd not connected.")

    def get_speed(self):
        cmd = obd.commands.SPEED
        response = self.connection.query(cmd)
        return response.value


def example():
    obd2 = OBD()
    try:
        while True:
            print(obd2.get_speed())
    except KeyboardInterrupt:
        pass
    
if __name__ == "__main__":
    example()