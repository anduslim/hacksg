from django.db import models

class SubZone(models.Model):
    AMK, BEDOK, BISHAN, BOONLAY, BKBATOK, BKMERAH, BKPANJANG, BKTIMAH, CENTRALWATER, CHANGI, CHANGIBAY, CCK, CLEMENTI, DOWNTOWN, GEYLANG, HOUGANG, JURONGEAST, JURONGWEST, KALLANG, LCK, MANDAI, MARINAEAST, MARINASOUTH, MPARADE, MUSEUM, NEWTON, NEISLAND, NOVENA, ORCHARD, OUTRAM, PASIRRIS, PAYALEBAR, PIONEER, PUNGGOL, QUEENSTOWN, RIVERVALLEY, ROCHER, SELETAR, SEMBAWANG, SENGKANG, SERANGOON, SIMPANG, SGRIVER, SISLAND, STRAITSVIEW, SUNGEIKADUT, TAMPINES, TANGLIN, TENGAH, TOAPAYOH, TUAS, WISLAND, WESTERNWATER, WOODLANDS, YISHUN = range(55)

    TOWNS_CHOICES = (
            (AMK, u'Ang Mo Kio'),
            (BEDOK, u'Bedok'),
            (BISHAN, u'Bishan'),
            (BOONLAY, u'Boon Lay'),
            (BKBATOK, u'Bukit Batok'),
            (BKMERAH, u'Bukit Merah'),
            (BKPANJANG, u'Bukit Panjang'),
            (BKTIMAH, u'Bukit Timah'),
            (CENTRALWATER, u'Central Water Catchment'),
            (CHANGI, u'Changi'),
            (CHANGIBAY, u'Changi Bay'),
            (CCK, u'Choa Chu Kang'),
            (CLEMENTI, u'Clementi'),
            (DOWNTOWN, u'Downtown Core'),
            (GEYLANG, u'Geylang'),
            (HOUGANG, u'Hougang'),
            (JURONGEAST, u'Jurong East'),
            (JURONGWEST, u'Jurong West'),
            (KALLANG, u'Kallang'),
            (LCK, u'Lim Chu Kang'),
            (MANDAI, u'Mandai'),
            (MARINAEAST, u'Marina East'),
            (MARINASOUTH, u'Marina South'),
            (MPARADE, u'Marine Parade'),
            (MUSEUM, u'Museum'),
            (NEWTON, u'Newton'),
            (NEISLAND, u'North-eastern Islands'),
            (NOVENA, u'Novena'),
            (ORCHARD, u'Orchard'),
            (OUTRAM, u'Outram'),
            (PASIRRIS, u'Pasir Ris'),
            (PAYALEBAR, u'Paya Lebar'),
            (PIONEER, u'Pioneer'),
            (PUNGGOL, u'Punggol'),
            (QUEENSTOWN, u'Queenstown'),
            (RIVERVALLEY, u'River Valley'),
            (ROCHER, u'Rocher'),
            (SELETAR, u'Seletar',),
            (SEMBAWANG, u'Sembawang'),
            (SENGKANG, u'Seng Kang'),
            (SERANGOON, u'Serangoon'),
            (SIMPANG, u'Simpang'),
            (SGRIVER, u'Singapore River'),
            (SISLAND, u'Southern Islands'),
            (STRAITSVIEW, u'Straits View'),
            (SUNGEIKADUT, u'Sungei Kadut'),
            (TAMPINES, u'Tampines'),
            (TANGLIN, u'Tanglin'),
            (TENGAH, u'Tengah'),
            (TOAPAYOH, u'Toa Payoh'),
            (TUAS, u'Tuas'),
            (WISLAND, u'Western Islands'),
            (WESTERNWATER, u'Western Water Catchment'),
            (WOODLANDS, u'Woodlands'),
            (YISHUN, u'Yishun')
        )

    town_name = models.PositiveSmallIntegerField(
                default=AMK,
                choices=TOWNS_CHOICES
                )

    name = models.CharField(max_length=150, blank=False)

    overall_score = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return ' '.join([self.get_town_name_display(), self.name])

class Category(models.Model):

    HOUSING, NEIGHBOURHOOD, TRANSPORTATION, ENVIRONMENT, HEALTH, ENGAGEMENT = range(6)

    CATEGORY_CHOICES = (
            (HOUSING, u'Housing'),
            (NEIGHBOURHOOD, u'Neighbourhood'),
            (TRANSPORTATION, u'Transportation'),
            (ENVIRONMENT, u'Environment'),
            (HEALTH, u'Health'),
            (ENGAGEMENT, u'Engagement')
        )

    category_type = models.PositiveSmallIntegerField(
        default=HOUSING,
        choices=CATEGORY_CHOICES
        )

    score = models.IntegerField(blank=False, default=0)

    subzone = models.ForeignKey('SubZone', blank=False, null=False, related_name='subzone_engagement')


class Amendity(models.Model):

    name = models.CharField(max_length=150, blank=False)

    value = models.IntegerField(blank=False)

    category_for = models.ForeignKey('Category', blank=False, null=False, related_name='Category_Amendity')


