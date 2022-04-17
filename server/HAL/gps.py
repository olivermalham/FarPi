import serial


class GPSPacket:

    # GPGGA parameters
    time = None                     # HHmmss
    latitude = None                 # dddmm.mmmm
    latitude_hemisphere = None      # N or S
    longitude = None                # dddmm.mmmm
    longitude_hemisphere = None     # W or E
    gps_fix = None                  # 0 = invalid, 1 = GPS fix, 2 = DGPS fix
    number_satellites = None        # satellites in view
    hdop = None                     # Relative accuracy of horizontal position
    altitude = None                 # meters
    altitude_units = None           # 'M' = meters
    geoid_wgs84 = None              # meters
    geoid_wgs84_units = None        # 'M' = meters
    time_since_dgps_update = None
    dgps_ref_station_id = None

    @staticmethod
    def new(*params):
        sentence_parts = params[0]
        sentence_type = sentence_parts[0][1:]
        if len(sentence_type) == 0:
            return None
        if sentence_type == "GPGGA":
            print(f"GPGGA fix data: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPGGA(params)

        if sentence_type == "GPGLL":
            print(f"GPGLL geo data: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPGLL(params)

        if sentence_type == "GPVTG":
            print(f"GPVTG ??: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPVTG(params)

        if sentence_type == "GPRMC":
            print(f"GPRMC ??: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPRMC(params)

        if sentence_type == "GPGSA":
            print(f"GPGSA ??: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPGSA(params)

        if sentence_type == "GPGSV":
            print(f"GPGSV ??: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPGSV(params)

        if sentence_type == "GPTXT":
            print(f"GPTXT info: {sentence_type} - {sentence_parts[1:]}")
            return GPSPacket.GPTXT(params)

    @staticmethod
    def GPGGA(*params):
        """
        Global positioning system fix data (time, position, fix type data)
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPGLL(*params):
        """
        Geographic position, latitude, longitude
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPVTG(*params):
        """
        Course and speed information relative to the ground
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPRMC(*params):
        """
        Time, date, position, course, and speed data
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPGSA(*params):
        """
        GPS receiver operating mode, satellites used in the position solution, and DOP values.
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPGSV(*params):
        """
        The number of GPS satellites in view, satellite ID numbers, elevation, azimuth, and SNR values.
        :param params:
        :return:
        """
        return GPSPacket()

    @staticmethod
    def GPTXT(*params):
        """
        Informational text?
        :param params:
        :return:
        """
        return GPSPacket()


GPS_SERIAL_PORT = "/dev/ttyACM0"
gps_serial = serial.Serial(GPS_SERIAL_PORT, 115200, timeout=0.2)

while True:
    data = gps_serial.readline()
    data = data.strip()
    data_parts = data.split(b",")
    packet = GPSPacket.new(data_parts)

