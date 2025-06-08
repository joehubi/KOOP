
from enum import Enum

class MemberEnum(Enum):
    HUBER_HOFFMANN      = (1, 'Huber/Hoffmann')
    TESSMANN            = (2, 'Teßmann')
    WENNINGER_FIEDLER   = (3, 'Wenninger/Fiedler')
    SONJA_GARTNER       = (4, 'Sonja Gartner')
    HILDEGUND_OSI       = (5, 'Hildegund & Osi')
    SARITA_SCHWERLA     = (6, 'Sarita Schwerla')
    LAUX                = (7, 'Laux')
    KLAUS_PLESSNER      = (8, 'Klaus Plessner')
    KOLLER              = (9, 'Koller')
    SUSANNE_ZEHETMEIER  = (10, 'Susanne Zehetmeier')
    FREI_11             = (11, '-')
    SCHUERKAEMPER       = (12, 'Schürkämper')
    GABI_MITSCHKA       = (13, 'Gabi Mitschka')
    FRITZ_SPOERL        = (14, 'Fritz Spörl')
    FREI_15             = (15, '-')
    FREI_0              = (0, '-')

    @property
    def nr(self):
        return self.value[0]

    @property
    def name(self):
        return self.value[1]

