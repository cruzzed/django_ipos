# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblAccSa(models.Model):
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc')
    tanggal = models.DateField(blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acc_sa'


class TblAccTmplrnr(models.Model):
    kodeacc = models.CharField(max_length=50, blank=True, null=True)
    urut = models.IntegerField(blank=True, null=True)
    tipeacc = models.CharField(max_length=5, blank=True, null=True)
    sub1 = models.CharField(max_length=100, blank=True, null=True)
    sub2 = models.CharField(max_length=100, blank=True, null=True)
    sub3 = models.CharField(max_length=100, blank=True, null=True)
    sub4 = models.CharField(max_length=100, blank=True, null=True)
    sub5 = models.CharField(max_length=100, blank=True, null=True)
    sub6 = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    setsub = models.IntegerField(blank=True, null=True)
    usergen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acc_tmplrnr'


class TblAccdepositdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblAccdeposithd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_accdepositdt'


class TblAccdeposithd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    kodeaccto = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeaccto', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tipe = models.CharField(max_length=30, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    tipetrs = models.CharField(max_length=30, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_accdeposithd'


class TblAccjurnal(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nourut = models.IntegerField(blank=True, null=True)
    tipeinput = models.CharField(max_length=5, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    posisi = models.CharField(max_length=5, blank=True, null=True)
    debet = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    kredit = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    kantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantor', blank=True, null=True)
    modul = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_accjurnal'


class TblAcckasdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblAcckashd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acckasdt'


class TblAcckashd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    kodeaccto = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeaccto', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tipe = models.CharField(max_length=30, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acckashd'


class TblAcctmpns(models.Model):
    kodeacc = models.CharField(max_length=30, blank=True, null=True)
    kelompok = models.CharField(max_length=5, blank=True, null=True)
    matauang = models.CharField(max_length=50, blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    rdebet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    rkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    debet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pdebet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tdebet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    lrdebet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    lrkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ndebet = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    usergen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acctmpns'


class TblAlamatkirim(models.Model):
    id = models.CharField(primary_key=True, max_length=150)
    kode_supel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kode_supel', blank=True, null=True)
    kontak = models.CharField(max_length=150, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    kota = models.CharField(max_length=100, blank=True, null=True)
    telepon = models.CharField(max_length=200, blank=True, null=True)
    kotatujuan = models.CharField(max_length=100, blank=True, null=True)
    kodekantor = models.CharField(max_length=50, blank=True, null=True)
    subwilasal = models.CharField(max_length=100, blank=True, null=True)
    subwiltujuan = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alamatkirim'


class TblBank(models.Model):
    kodebank = models.CharField(primary_key=True, max_length=30)
    namabank = models.CharField(max_length=100, blank=True, null=True)
    acc_kd = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kd', blank=True, null=True)
    acc_kk = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bank'


class TblByrhutangdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.ForeignKey('TblByrhutanghd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    notrsmasuk = models.ForeignKey('TblImhd', models.DO_NOTHING, db_column='notrsmasuk', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    ratetrs = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrhutangdt'


class TblByrhutanghd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalpotongan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_bayar = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bayar', blank=True, null=True)
    acc_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pot', blank=True, null=True)
    carabayar = models.CharField(max_length=5, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    nomor = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    stslunas = models.BooleanField(blank=True, null=True)
    tgllunas_cbg = models.DateTimeField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrhutanghd'


class TblByrhutangitem(models.Model):
    iddetail = models.ForeignKey(TblByrhutangdt, models.DO_NOTHING, db_column='iddetail', blank=True, null=True)
    iddetailitem = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.ForeignKey(TblByrhutanghd, models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmllaku = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrhutangitem'


class TblByrhutangkonsidt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.ForeignKey('TblByrhutangkonsihd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    notrsmasuk = models.ForeignKey('TblTagihimhd', models.DO_NOTHING, db_column='notrsmasuk', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    ratetrs = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrhutangkonsidt'


class TblByrhutangkonsihd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalpotongan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_bayar = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bayar', blank=True, null=True)
    acc_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pot', blank=True, null=True)
    carabayar = models.CharField(max_length=5, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    nomor = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    stslunas = models.BooleanField(blank=True, null=True)
    xx = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tgllunas_cbg = models.DateTimeField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrhutangkonsihd'


class TblByrkomisislsdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.ForeignKey('TblByrkomisislshd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    notrsmasuk = models.CharField(max_length=50, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    ratetrs = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    kodesupel = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrkomisislsdt'


class TblByrkomisislshd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_bayar = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bayar', blank=True, null=True)
    acc_komisi_sales = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_komisi_sales', blank=True, null=True)
    carabayar = models.CharField(max_length=5, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    nomor = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    stslunas = models.BooleanField(blank=True, null=True)
    periodetgl1 = models.DateTimeField(blank=True, null=True)
    periodetgl2 = models.DateTimeField(blank=True, null=True)
    tgllunas_cbg = models.DateTimeField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrkomisislshd'


class TblByrpiutangdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.ForeignKey('TblByrpiutanghd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    notrsmasuk = models.CharField(max_length=50, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    ratetrs = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrpiutangdt'


class TblByrpiutanghd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalpotongan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_bayar = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bayar', blank=True, null=True)
    acc_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pot', blank=True, null=True)
    carabayar = models.CharField(max_length=5, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    nomor = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    stslunas = models.BooleanField(blank=True, null=True)
    tgllunas_cbg = models.DateTimeField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrpiutanghd'


class TblByrpiutangkonsidt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.ForeignKey('TblByrpiutangkonsihd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    notrsmasuk = models.ForeignKey('TblTagihikhd', models.DO_NOTHING, db_column='notrsmasuk', blank=True, null=True)
    tipe = models.CharField(max_length=5, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    ratetrs = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrpiutangkonsidt'


class TblByrpiutangkonsihd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=5, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    totalbayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalpotongan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_bayar = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bayar', blank=True, null=True)
    acc_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pot', blank=True, null=True)
    carabayar = models.CharField(max_length=5, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    nomor = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    stslunas = models.BooleanField(blank=True, null=True)
    tgllunas_cbg = models.DateTimeField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_byrpiutangkonsihd'


class TblConf(models.Model):
    confname = models.CharField(primary_key=True, max_length=50)
    confvalue = models.CharField(max_length=254, blank=True, null=True)
    confblob = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_conf'


class TblEmoney(models.Model):
    kodeprod = models.CharField(primary_key=True, max_length=30)
    namaprod = models.CharField(max_length=100, blank=True, null=True)
    acc_prod = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_prod', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emoney'


class TblFormatnosp(models.Model):
    trid = models.CharField(primary_key=True, max_length=5)
    nomor = models.BigIntegerField(blank=True, null=True)
    slot1 = models.CharField(max_length=10, blank=True, null=True)
    slot2 = models.CharField(max_length=10, blank=True, null=True)
    slot3 = models.CharField(max_length=10, blank=True, null=True)
    sep1 = models.CharField(max_length=2, blank=True, null=True)
    sep2 = models.CharField(max_length=2, blank=True, null=True)
    numdgt = models.IntegerField(blank=True, null=True)
    lastnom = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_formatnosp'


class TblFormatnotr(models.Model):
    trid = models.CharField(primary_key=True, max_length=10)
    nomor = models.BigIntegerField(blank=True, null=True)
    slot1 = models.CharField(max_length=10, blank=True, null=True)
    slot2 = models.CharField(max_length=10, blank=True, null=True)
    slot3 = models.CharField(max_length=10, blank=True, null=True)
    slot4 = models.CharField(max_length=10, blank=True, null=True)
    slot5 = models.CharField(max_length=10, blank=True, null=True)
    sep1 = models.CharField(max_length=2, blank=True, null=True)
    sep2 = models.CharField(max_length=2, blank=True, null=True)
    sep3 = models.CharField(max_length=2, blank=True, null=True)
    sep4 = models.CharField(max_length=2, blank=True, null=True)
    resetid = models.CharField(max_length=10, blank=True, null=True)
    numdgt = models.IntegerField(blank=True, null=True)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    kantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantor')
    lastgen = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_formatnotr'
        unique_together = (('trid', 'kantor'),)


class TblHupiSa(models.Model):
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    kode_acc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kode_acc', blank=True, null=True)
    kodemu = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='kodemu', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    tipetrs = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_hupi_sa'


class TblIkdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblIkhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlpesan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan2 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan3 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan4 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrmasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlsisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsibayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    idorder = models.CharField(max_length=150, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    idtrsretur = models.CharField(max_length=150, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    notrsretur = models.CharField(max_length=100, blank=True, null=True)
    potpiutang = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    jmlterimajadi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sistemhargajual = models.CharField(max_length=1, blank=True, null=True)
    tipepromo = models.CharField(max_length=15, blank=True, null=True)
    jmlgratis = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    itempromo = models.CharField(max_length=100, blank=True, null=True)
    satuanpromo = models.CharField(max_length=50, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tebus = models.BooleanField(blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ikdt'


class TblIkhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantordari = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantordari', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notrsorder = models.CharField(max_length=50, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    kodesales = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales', blank=True, null=True)
    kodesales2 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales2', blank=True, null=True)
    kodesales3 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales3', blank=True, null=True)
    kodesales4 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales4', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitempesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajak = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    carabayar = models.CharField(max_length=20, blank=True, null=True)
    jmltunai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmldebit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    notrsretur = models.ForeignKey('self', models.DO_NOTHING, db_column='notrsretur', blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    totalkotagih = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_potongan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_potongan', blank=True, null=True)
    acc_pajak = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pajak', blank=True, null=True)
    acc_biayalain = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biayalain', blank=True, null=True)
    acc_tunai = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_tunai', blank=True, null=True)
    acc_kredit = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kredit', blank=True, null=True)
    acc_sales = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_sales', blank=True, null=True)
    acc_hpp = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_debit = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_debit', blank=True, null=True)
    acc_kk = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kk', blank=True, null=True)
    acc_deposit = models.CharField(max_length=30, blank=True, null=True)
    acc_sales_hut = models.CharField(max_length=30, blank=True, null=True)
    acc_biaya_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    acc_dppesanan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_beda_cab = models.CharField(max_length=30, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    byr_krd_no = models.CharField(max_length=30, blank=True, null=True)
    byr_debit_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_debit_bank', blank=True, null=True)
    byr_kk_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_kk_bank', blank=True, null=True)
    byr_debit_no = models.CharField(max_length=100, blank=True, null=True)
    byr_kk_no = models.CharField(max_length=100, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmldeposit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    point_ik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    point_sts = models.IntegerField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    tanggal_sa = models.DateField(blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    nofp = models.CharField(max_length=100, blank=True, null=True)
    byr_komisi1 = models.BooleanField(blank=True, null=True)
    byr_komisi2 = models.BooleanField(blank=True, null=True)
    byr_komisi3 = models.BooleanField(blank=True, null=True)
    byr_komisi4 = models.BooleanField(blank=True, null=True)
    point_notrans = models.CharField(max_length=50, blank=True, null=True)
    totalterimajadi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ak_kotatujuan = models.CharField(max_length=100, blank=True, null=True)
    opsikirim = models.CharField(max_length=5, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    ambilnomor = models.CharField(max_length=50, blank=True, null=True)
    jumlah_cetak = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    status_online = models.BooleanField(blank=True, null=True)
    compname_online = models.CharField(max_length=255, blank=True, null=True)
    user_online = models.CharField(max_length=50, blank=True, null=True)
    mode_retur = models.CharField(max_length=5, blank=True, null=True)
    jmlemoney = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    byr_emoney_no = models.CharField(max_length=100, blank=True, null=True)
    byr_emoney_prod = models.ForeignKey(TblEmoney, models.DO_NOTHING, db_column='byr_emoney_prod', blank=True, null=True)
    acc_emoney = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_emoney', blank=True, null=True)
    selisihpembulatan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_pend_pembulatan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pend_pembulatan', blank=True, null=True)
    kodevoucher = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ikhd'


class TblIkrakitan(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailtrs = models.ForeignKey(TblIkdt, models.DO_NOTHING, db_column='iddetailtrs', blank=True, null=True)
    notransaksi = models.ForeignKey(TblIkhd, models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodeitem = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodeitemrakitan = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitemrakitan', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jumlahtrs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuantrs = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    jenisrakit = models.CharField(max_length=20, blank=True, null=True)
    totalhppitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ikrakitan'


class TblImdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblImhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlpesan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hargadsr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuandsr = models.CharField(max_length=50, blank=True, null=True)
    jmlmasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrmasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlsisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsibayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    idtrsretur = models.CharField(max_length=150, blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)
    idorder = models.CharField(max_length=150, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    sakantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='sakantor', blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    pothutang = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    notrsretur = models.CharField(max_length=100, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    jmlprosesrakit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmltagihki = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potongan2 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan3 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan4 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_imdt'


class TblImhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantortujuan = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantortujuan', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notrsorder = models.CharField(max_length=50, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitempesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajak = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmldeposit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    carabayar = models.CharField(max_length=20, blank=True, null=True)
    jmltunai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    byr_krd_no = models.CharField(max_length=30, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    notrsretur = models.ForeignKey('self', models.DO_NOTHING, db_column='notrsretur', blank=True, null=True)
    acc_potongan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_potongan', blank=True, null=True)
    acc_pajak = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pajak', blank=True, null=True)
    acc_biayalain = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biayalain', blank=True, null=True)
    acc_tunai = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_tunai', blank=True, null=True)
    acc_kredit = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kredit', blank=True, null=True)
    acc_hpp = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_deposit = models.CharField(max_length=30, blank=True, null=True)
    acc_dppesanan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_biaya_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    acc_beda_cab = models.CharField(max_length=30, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    tanggal_sa = models.DateField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    tottagihki = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totitemretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    swt_sa_sts = models.BooleanField(blank=True, null=True)
    prpotfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    nofp = models.CharField(max_length=100, blank=True, null=True)
    status_online = models.BooleanField(blank=True, null=True)
    compname_online = models.CharField(max_length=255, blank=True, null=True)
    user_online = models.CharField(max_length=50, blank=True, null=True)
    mode_retur = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_imhd'


class TblImrakitan(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.ForeignKey(TblImhd, models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodeitem = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodeitemrakitan = models.ForeignKey('TblItem', models.DO_NOTHING, db_column='kodeitemrakitan', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.CharField(max_length=50, blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jumlahtrs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuantrs = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_imrakitan'


class TblInfodb(models.Model):
    versidb = models.CharField(max_length=255, blank=True, null=True)
    versiupdate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_infodb'


class TblItem(models.Model):
    kodeitem = models.CharField(primary_key=True, max_length=100)
    namaitem = models.TextField(blank=True, null=True)
    jenis = models.ForeignKey('TblItemjenis', models.DO_NOTHING, db_column='jenis', blank=True, null=True)
    tipe = models.CharField(max_length=15, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    serial = models.CharField(max_length=15, blank=True, null=True)
    konsinyasi = models.CharField(max_length=15, blank=True, null=True)
    stokmin = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sistemhargajual = models.CharField(max_length=1, blank=True, null=True)
    opsihargajual = models.BooleanField(blank=True, null=True)
    rak = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    hargapokok = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    prhargajual1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hargajual1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    supplier1 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='supplier1', blank=True, null=True)
    supplier2 = models.CharField(max_length=50, blank=True, null=True)
    supplier3 = models.CharField(max_length=50, blank=True, null=True)
    gambar = models.BinaryField(blank=True, null=True)
    statusjual = models.CharField(max_length=15, blank=True, null=True)
    merek = models.ForeignKey('TblItemmerek', models.DO_NOTHING, db_column='merek', blank=True, null=True)
    hppsys = models.CharField(max_length=10, blank=True, null=True)
    sistempajak = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    opsiflexhargajual = models.BooleanField(blank=True, null=True)
    hargarakit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    statushapus = models.CharField(max_length=15, blank=True, null=True)
    stok = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dept = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='dept', blank=True, null=True)
    pendingin = models.CharField(max_length=15, blank=True, null=True)
    acc_hpp = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_pendapatan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pendapatan', blank=True, null=True)
    acc_persediaan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_persediaan', blank=True, null=True)
    acc_jasa = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_jasa', blank=True, null=True)
    acc_noninventory = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_noninventory', blank=True, null=True)
    acc_perbahanbaku = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_perbahanbaku', blank=True, null=True)
    acc_bytenagakerja = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_bytenagakerja', blank=True, null=True)
    acc_byoverhead = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_byoverhead', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    tmphp = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tmpjml = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tmpnilai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    gambarfiles = models.TextField(blank=True, null=True)
    tanggal_add = models.DateTimeField(blank=True, null=True)
    opsihargarakitan = models.BooleanField(blank=True, null=True)
    nonpajakex = models.BooleanField(blank=True, null=True)
    opsidefhargapokok = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item'


class TblItemIk(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailim = models.CharField(max_length=150)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahdasar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuandasar = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuandasar', blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkotagih = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    iddetailserial = models.CharField(max_length=150, blank=True, null=True)
    origin_tipe = models.CharField(max_length=20, blank=True, null=True)
    origin_iddt = models.CharField(max_length=150, blank=True, null=True)
    ori_iddetail = models.CharField(max_length=150, blank=True, null=True)
    ori_tipe = models.CharField(max_length=20, blank=True, null=True)
    noserial = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_ik'


class TblItemIkko(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailik = models.CharField(max_length=150, blank=True, null=True)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    iddetailserial = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_ikko'


class TblItemIkret(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailik = models.CharField(max_length=150, blank=True, null=True)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahdasar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    origin_tipe = models.CharField(max_length=20, blank=True, null=True)
    origin_iddt = models.CharField(max_length=150, blank=True, null=True)
    ori_iddetail = models.CharField(max_length=150, blank=True, null=True)
    ori_tipe = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_ikret'


class TblItemIm(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tgl_trs = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahdasar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuandasar = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuandasar', blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    masuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    remasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    rekeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    transfer = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keluar_konsi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    rekeluar_konsi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    remasuk_konsi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    sisa_konsi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    flagavg = models.SmallIntegerField(blank=True, null=True)
    origin_iddt = models.CharField(max_length=150, blank=True, null=True)
    origin_tipe = models.CharField(max_length=20, blank=True, null=True)
    ori_iddetail = models.CharField(max_length=150, blank=True, null=True)
    ori_tipe = models.CharField(max_length=20, blank=True, null=True)
    ori_id_trf = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_im'


class TblItemImret(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailim = models.CharField(max_length=150, blank=True, null=True)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahdasar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hargadasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    idtrsserial = models.CharField(max_length=150, blank=True, null=True)
    ori_iddetail = models.CharField(max_length=150, blank=True, null=True)
    ori_tipe = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_imret'


class TblItemRekap(models.Model):
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    bulan = models.IntegerField(blank=True, null=True)
    tahun = models.IntegerField(blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    awal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    awal_nilai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    awal_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    masuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    masuk_nilai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    masuk_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keluar_nilai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keluar_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    akhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    akhir_nilai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    akhir_total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_rekap'


class TblItemSa(models.Model):
    iddetailtrs = models.CharField(primary_key=True, max_length=150)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tgl_trs = models.DateTimeField(blank=True, null=True)
    nobaris = models.IntegerField(blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_item_sa'


class TblItemdisp(models.Model):
    iddiskon = models.CharField(primary_key=True, max_length=50)
    kodeitemd = models.CharField(max_length=100, blank=True, null=True)
    kodeitems = models.CharField(max_length=100, blank=True, null=True)
    jenis = models.ForeignKey('TblItemjenis', models.DO_NOTHING, db_column='jenis', blank=True, null=True)
    merek = models.ForeignKey('TblItemmerek', models.DO_NOTHING, db_column='merek', blank=True, null=True)
    tgldari = models.DateTimeField(blank=True, null=True)
    tglsampai = models.DateTimeField(blank=True, null=True)
    pot1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    stsact = models.BooleanField(blank=True, null=True)
    tipeper = models.CharField(max_length=10, blank=True, null=True)
    jamdari = models.DateTimeField(blank=True, null=True)
    jamsampai = models.DateTimeField(blank=True, null=True)
    w1 = models.BooleanField(blank=True, null=True)
    w2 = models.BooleanField(blank=True, null=True)
    w3 = models.BooleanField(blank=True, null=True)
    w4 = models.BooleanField(blank=True, null=True)
    w5 = models.BooleanField(blank=True, null=True)
    w6 = models.BooleanField(blank=True, null=True)
    w7 = models.BooleanField(blank=True, null=True)
    prioritas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    stsvcr = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemdisp'


class TblItemdispdt(models.Model):
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    opsidiskon = models.IntegerField(blank=True, null=True)
    diskon1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    diskon2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    diskon3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    diskon4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    disknom1 = models.DecimalField(max_digits=40, decimal_places=20, blank=True, null=True)
    disknom2 = models.DecimalField(max_digits=40, decimal_places=20, blank=True, null=True)
    disknom3 = models.DecimalField(max_digits=40, decimal_places=20, blank=True, null=True)
    disknom4 = models.DecimalField(max_digits=40, decimal_places=20, blank=True, null=True)
    iddiskon = models.ForeignKey(TblItemdisp, models.DO_NOTHING, db_column='iddiskon', blank=True, null=True)
    kgruppel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemdispdt'


class TblItemhj(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    tipehj = models.CharField(max_length=10, blank=True, null=True)
    jmlsampai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    prosentase = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    hargajual = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemhj'


class TblItemjenis(models.Model):
    jenis = models.CharField(primary_key=True, max_length=50)
    ketjenis = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemjenis'


class TblItemketerangan(models.Model):
    kodeket = models.CharField(primary_key=True, max_length=50)
    keterangan = models.CharField(max_length=300, blank=True, null=True)
    jenisket = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_itemketerangan'
        unique_together = (('kodeket', 'jenisket'),)


class TblItemmerek(models.Model):
    merek = models.CharField(primary_key=True, max_length=50)
    ketmerek = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemmerek'


class TblItemopname(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    periode = models.CharField(max_length=20, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem')
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    jmlsebelum = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlfisik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlselisih = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemopname'


class TblItempotongan(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodegrup = models.ForeignKey('TblSupelgrup', models.DO_NOTHING, db_column='kodegrup', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pot4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itempotongan'


class TblItempromo(models.Model):
    idpromo = models.CharField(primary_key=True, max_length=50)
    kodeitemd = models.CharField(max_length=100, blank=True, null=True)
    kodeitems = models.CharField(max_length=100, blank=True, null=True)
    jenis = models.ForeignKey(TblItemjenis, models.DO_NOTHING, db_column='jenis', blank=True, null=True)
    merek = models.ForeignKey(TblItemmerek, models.DO_NOTHING, db_column='merek', blank=True, null=True)
    tgldari = models.DateTimeField(blank=True, null=True)
    tglsampai = models.DateTimeField(blank=True, null=True)
    stsact = models.BooleanField(blank=True, null=True)
    tipeper = models.CharField(max_length=10, blank=True, null=True)
    jamdari = models.DateTimeField(blank=True, null=True)
    jamsampai = models.DateTimeField(blank=True, null=True)
    w1 = models.BooleanField(blank=True, null=True)
    w2 = models.BooleanField(blank=True, null=True)
    w3 = models.BooleanField(blank=True, null=True)
    w4 = models.BooleanField(blank=True, null=True)
    w5 = models.BooleanField(blank=True, null=True)
    w6 = models.BooleanField(blank=True, null=True)
    w7 = models.BooleanField(blank=True, null=True)
    prioritas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itempromo'


class TblItempromodt(models.Model):
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlahjual = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuanjual = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuanjual', blank=True, null=True)
    jumlahgratis = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuangratis = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuangratis', blank=True, null=True)
    idpromo = models.ForeignKey(TblItempromo, models.DO_NOTHING, db_column='idpromo', blank=True, null=True)
    kodeitemgr = models.CharField(max_length=100, blank=True, null=True)
    kelipatan = models.BooleanField(blank=True, null=True)
    tebus = models.BooleanField(blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    opsigratis = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itempromodt'


class TblItemrakitan(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=100)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodeitemrakitan = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitemrakitan', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey('TblItemsatuan', models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemrakitan'


class TblItemsatuan(models.Model):
    satuan = models.CharField(primary_key=True, max_length=50)
    ketsatuan = models.CharField(max_length=100, blank=True, null=True)
    konversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuankonversi = models.CharField(max_length=50, blank=True, null=True)
    utama = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemsatuan'


class TblItemsatuanjml(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    jumlahkonv = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kodebarcode = models.CharField(unique=True, max_length=100, blank=True, null=True)
    hargapokok = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    poin = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    komisisales = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemsatuanjml'


class TblItemserial(models.Model):
    noserial = models.CharField(primary_key=True, max_length=255)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    origin_tipe = models.CharField(max_length=20, blank=True, null=True)
    origin_iddt = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemserial'


class TblItemserialKotag(models.Model):
    noserial = models.CharField(primary_key=True, max_length=255)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    kodekantor = models.CharField(max_length=50, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemserial_kotag'


class TblItemserialdt(models.Model):
    noserial = models.CharField(max_length=255, blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    serialtipe = models.CharField(max_length=20, blank=True, null=True)
    serialiddetail = models.CharField(max_length=150, blank=True, null=True)
    iddetailrakitan = models.CharField(max_length=150, blank=True, null=True)
    idtrsretur = models.CharField(max_length=150, blank=True, null=True)
    statuskotag = models.CharField(max_length=15, blank=True, null=True)
    origin_tipe = models.CharField(max_length=20, blank=True, null=True)
    origin_iddt = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemserialdt'


class TblItemserialmanage(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    periode = models.CharField(max_length=20, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem')
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    jmlsebelum = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlfisik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlselisih = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kodeacc = models.CharField(max_length=30, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    jmlserial = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemserialmanage'


class TblItemstok(models.Model):
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantor', blank=True, null=True)
    stok = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itemstok'


class TblItktdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblItkthd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlpesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan2 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan3 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan4 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrmasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlsisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsibayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    idorder = models.CharField(max_length=150, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    idtrsretur = models.CharField(max_length=150, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    notrsretur = models.CharField(max_length=100, blank=True, null=True)
    potpiutang = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    jmlterimajadi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    sistemhargajual = models.CharField(max_length=1, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itktdt'


class TblItkthd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantordari = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantordari', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notrsorder = models.CharField(max_length=50, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    kodesales = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales', blank=True, null=True)
    kodesales2 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales2', blank=True, null=True)
    kodesales3 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales3', blank=True, null=True)
    kodesales4 = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales4', blank=True, null=True)
    matauang = models.ForeignKey('TblMatauang', models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    totalitemin = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitemout = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitempesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtoin = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotout = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajakin = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajakin = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    pajakout = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajakout = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    carabayar = models.CharField(max_length=20, blank=True, null=True)
    jmltunai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmldebit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nofp = models.CharField(max_length=100, blank=True, null=True)
    acc_potongan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_potongan', blank=True, null=True)
    acc_pajak_in = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pajak_in', blank=True, null=True)
    acc_pajak = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_pajak', blank=True, null=True)
    acc_biayalain = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biayalain', blank=True, null=True)
    acc_tunai = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_tunai', blank=True, null=True)
    acc_kredit = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kredit', blank=True, null=True)
    acc_sales = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_sales', blank=True, null=True)
    acc_hpp = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_debit = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_debit', blank=True, null=True)
    acc_kk = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_kk', blank=True, null=True)
    acc_deposit = models.CharField(max_length=30, blank=True, null=True)
    acc_dppesanan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_biaya_pot = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    byr_krd_no = models.CharField(max_length=30, blank=True, null=True)
    byr_debit_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_debit_bank', blank=True, null=True)
    byr_kk_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_kk_bank', blank=True, null=True)
    byr_debit_no = models.CharField(max_length=100, blank=True, null=True)
    byr_kk_no = models.CharField(max_length=100, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    tanggal_sa = models.DateField(blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    point_ik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    point_sts = models.IntegerField(blank=True, null=True)
    notrsretur = models.ForeignKey(TblIkhd, models.DO_NOTHING, db_column='notrsretur', blank=True, null=True)
    point_notrans = models.CharField(max_length=50, blank=True, null=True)
    jmldeposit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    byr_komisi1 = models.BooleanField(blank=True, null=True)
    byr_komisi2 = models.BooleanField(blank=True, null=True)
    byr_komisi3 = models.BooleanField(blank=True, null=True)
    byr_komisi4 = models.BooleanField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    status_online = models.BooleanField(blank=True, null=True)
    compname_online = models.CharField(max_length=255, blank=True, null=True)
    user_online = models.CharField(max_length=50, blank=True, null=True)
    jmlemoney = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    byr_emoney_no = models.CharField(max_length=100, blank=True, null=True)
    byr_emoney_prod = models.ForeignKey(TblEmoney, models.DO_NOTHING, db_column='byr_emoney_prod', blank=True, null=True)
    acc_emoney = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_emoney', blank=True, null=True)
    acc_sales_hut = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itkthd'


class TblItrdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblItrhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    hppdasar = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itrdt'


class TblItrhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantordari = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantordari', blank=True, null=True)
    kantortujuan = models.ForeignKey('TblKantor', models.DO_NOTHING, db_column='kantortujuan', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    acc_persediaan = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='acc_persediaan', blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    mob_owner_id = models.CharField(max_length=20, blank=True, null=True)
    mob_trf_sts = models.BooleanField(blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    status_online = models.BooleanField(blank=True, null=True)
    compname_online = models.CharField(max_length=255, blank=True, null=True)
    user_online = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_itrhd'


class TblKantor(models.Model):
    kodekantor = models.CharField(primary_key=True, max_length=50)
    fungsi = models.CharField(max_length=20, blank=True, null=True)
    namakantor = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    notelepon = models.CharField(max_length=150, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    cabang = models.BooleanField(blank=True, null=True)
    kodeacc = models.ForeignKey('TblPerkiraan', models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    mobile = models.BooleanField(blank=True, null=True)
    stspakai = models.BooleanField(blank=True, null=True)
    nompajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    stsaktif = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_kantor'


class TblKaslaci(models.Model):
    nama_user = models.CharField(max_length=50)
    shift = models.CharField(max_length=10, blank=True, null=True)
    kas_awal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kas_masuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    kas_akhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    wkt_mulai = models.DateTimeField(blank=True, null=True)
    wkt_akhir = models.DateTimeField(blank=True, null=True)
    login_flag = models.BooleanField(blank=True, null=True)
    kas_keluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nama_komputer = models.CharField(max_length=20, blank=True, null=True)
    notransaksi = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_kaslaci'


class TblKaslacidt(models.Model):
    notransaksi = models.ForeignKey(TblKaslaci, models.DO_NOTHING, db_column='notransaksi')
    nama_pengambil = models.CharField(max_length=50, blank=True, null=True)
    kas_keluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keterangan_p = models.CharField(max_length=100, blank=True, null=True)
    iddetail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tbl_kaslacidt'


class TblLogaktivitasAkuntansi(models.Model):
    object = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    kodeacc = models.CharField(max_length=50, blank=True, null=True)
    cmd = models.CharField(max_length=20)
    user1 = models.CharField(max_length=30)
    shift = models.CharField(max_length=20, blank=True, null=True)
    compname = models.CharField(max_length=200)
    kodekantor = models.CharField(max_length=20)
    dateupd = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=100)
    nama_app = models.CharField(max_length=20, blank=True, null=True)
    versi_app = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_logaktivitas_akuntansi'


class TblLogaktivitasImpor(models.Model):
    object = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100)
    user1 = models.CharField(max_length=30)
    shift = models.CharField(max_length=20, blank=True, null=True)
    compname = models.CharField(max_length=200)
    kodekantor = models.CharField(max_length=20)
    dateupd = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=100)
    nama_app = models.CharField(max_length=20, blank=True, null=True)
    versi_app = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_logaktivitas_impor'


class TblLogaktivitasMaster(models.Model):
    object = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100)
    cmd = models.CharField(max_length=20)
    user1 = models.CharField(max_length=30)
    shift = models.CharField(max_length=20, blank=True, null=True)
    compname = models.CharField(max_length=200)
    kodekantor = models.CharField(max_length=20)
    dateupd = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=100)
    nama_app = models.CharField(max_length=20, blank=True, null=True)
    versi_app = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_logaktivitas_master'


class TblLogaktivitasSistem(models.Model):
    object = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    cmd = models.CharField(max_length=20)
    user1 = models.CharField(max_length=30)
    shift = models.CharField(max_length=20, blank=True, null=True)
    kodekantor = models.CharField(max_length=20)
    nama_app = models.CharField(max_length=20, blank=True, null=True)
    versi_app = models.CharField(max_length=100, blank=True, null=True)
    dateupd = models.DateTimeField()
    compname = models.CharField(max_length=200)
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'tbl_logaktivitas_sistem'


class TblLogaktivitasTransaksi(models.Model):
    object = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100)
    iddetail = models.CharField(max_length=150, blank=True, null=True)
    notransaksi = models.CharField(max_length=100, blank=True, null=True)
    cmd = models.CharField(max_length=20)
    user1 = models.CharField(max_length=30)
    shift = models.CharField(max_length=20, blank=True, null=True)
    kodekantor = models.CharField(max_length=20)
    dateupd = models.DateTimeField()
    compname = models.CharField(max_length=200)
    id = models.CharField(primary_key=True, max_length=100)
    nama_app = models.CharField(max_length=20, blank=True, null=True)
    versi_app = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_logaktivitas_transaksi'


class TblMatauang(models.Model):
    matauang = models.CharField(primary_key=True, max_length=50)
    ketmatauang = models.CharField(max_length=100, blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    utama = models.BooleanField(blank=True, null=True)
    acc_hutang = models.CharField(max_length=50, blank=True, null=True)
    acc_piutang = models.CharField(max_length=50, blank=True, null=True)
    acc_byrtunai = models.CharField(max_length=50, blank=True, null=True)
    acc_byrbank = models.CharField(max_length=50, blank=True, null=True)
    tipe = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_matauang'


class TblMuRatesa(models.Model):
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mu_ratesa'


class TblOngkir(models.Model):
    id = models.CharField(primary_key=True, max_length=150)
    expedisi = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=100, blank=True, null=True)
    negara = models.CharField(max_length=100, blank=True, null=True)
    biaya1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biaya2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biaya3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    kotatujuan = models.CharField(max_length=100, blank=True, null=True)
    kodekantor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ongkir'


class TblPengiriman(models.Model):
    notrs = models.CharField(primary_key=True, max_length=50)
    idalamat_kirim = models.CharField(max_length=150, blank=True, null=True)
    idongkir_kurir = models.CharField(max_length=150, blank=True, null=True)
    berat = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    paket = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    statuskirim = models.CharField(max_length=50, blank=True, null=True)
    tanggalkirim = models.DateTimeField(blank=True, null=True)
    noresi = models.CharField(max_length=150, blank=True, null=True)
    kurir = models.CharField(max_length=150, blank=True, null=True)
    jasa = models.CharField(max_length=50, blank=True, null=True)
    layanan = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    opsioffline = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pengiriman'


class TblPerkiraan(models.Model):
    kodeacc = models.CharField(primary_key=True, max_length=30)
    parentacc = models.ForeignKey('self', models.DO_NOTHING, db_column='parentacc', blank=True, null=True)
    kelompok = models.CharField(max_length=2, blank=True, null=True)
    tipe = models.CharField(max_length=2, blank=True, null=True)
    namaacc = models.CharField(max_length=200, blank=True, null=True)
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    kasbank = models.BooleanField(blank=True, null=True)
    defmuutm = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_perkiraan'


class TblPerksetting(models.Model):
    accsetting = models.CharField(max_length=50)
    kodeacc = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='kodeacc', blank=True, null=True)
    acckantor = models.OneToOneField(TblKantor, models.DO_NOTHING, db_column='acckantor', primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbl_perksetting'
        unique_together = (('acckantor', 'accsetting'),)


class TblPesandt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblPesanhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlterima = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    sistemhargajual = models.CharField(max_length=1, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pesandt'


class TblPesanhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantortujuan = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kantortujuan', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    tanggalkirim = models.DateTimeField(blank=True, null=True)
    jenis = models.CharField(max_length=20, blank=True, null=True)
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    kodesales = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesales', blank=True, null=True)
    kodesales2 = models.CharField(max_length=50, blank=True, null=True)
    kodesales3 = models.CharField(max_length=50, blank=True, null=True)
    kodesales4 = models.CharField(max_length=50, blank=True, null=True)
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    komisi1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalterima = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajak = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dppesananbyr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_dppesanan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_dpkas = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_dpkas', blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)
    prpotfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    acc_biaya_pot = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    opsikirim = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pesanhd'


class TblPesanrakitan(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    iddetailtrs = models.ForeignKey(TblPesandt, models.DO_NOTHING, db_column='iddetailtrs', blank=True, null=True)
    notransaksi = models.ForeignKey(TblPesanhd, models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    kodeitemrakitan = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitemrakitan', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jumlahtrs = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuantrs = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    jenisrakit = models.CharField(max_length=20, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pesanrakitan'


class TblPointSa(models.Model):
    kodesupel = models.ForeignKey('TblSupel', models.DO_NOTHING, db_column='kodesupel')
    kodekantor = models.CharField(max_length=50, blank=True, null=True)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    point_ik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_point_sa'


class TblPointambil(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    tipe = models.CharField(max_length=50, blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    periodetgl1 = models.DateTimeField(blank=True, null=True)
    periodetgl2 = models.DateTimeField(blank=True, null=True)
    jmlambil = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    kodesupel = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    kodekantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pointambil'


class TblRbHutang(models.Model):
    noretur = models.ForeignKey(TblImhd, models.DO_NOTHING, db_column='noretur', blank=True, null=True)
    notrspot = models.ForeignKey(TblImhd, models.DO_NOTHING, db_column='notrspot', blank=True, null=True)
    jmlpot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rb_hutang'


class TblRefRetur(models.Model):
    iddetail = models.CharField(max_length=150)
    notransaksi = models.CharField(max_length=50, blank=True, null=True)
    iddetailim = models.CharField(max_length=150, blank=True, null=True)
    kodeitem = models.CharField(max_length=150, blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ref_retur'


class TblRequestUploadQueue(models.Model):
    idupload = models.CharField(primary_key=True, max_length=100)
    entry_date = models.DateTimeField(blank=True, null=True)
    modul_type = models.CharField(max_length=50, blank=True, null=True)
    modul_key_value = models.CharField(max_length=255, blank=True, null=True)
    modul_key_oldvalue = models.CharField(max_length=255, blank=True, null=True)
    save_type = models.CharField(max_length=50, blank=True, null=True)
    flag_upload = models.IntegerField(blank=True, null=True)
    ret_id = models.CharField(max_length=20, blank=True, null=True)
    ret_msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_request_upload_queue'


class TblRjPiutang(models.Model):
    noretur = models.ForeignKey(TblIkhd, models.DO_NOTHING, db_column='noretur', blank=True, null=True)
    notrspot = models.ForeignKey(TblIkhd, models.DO_NOTHING, db_column='notrspot', blank=True, null=True)
    jmlpot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rj_piutang'


class TblSandi(models.Model):
    angka = models.CharField(max_length=2, blank=True, null=True)
    huruf = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sandi'


class TblSettingpel(models.Model):
    ptipe = models.IntegerField(blank=True, null=True)
    pkelipatan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pnilaitukar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pmasadari = models.DateTimeField(blank=True, null=True)
    pmasasampai = models.DateTimeField(blank=True, null=True)
    pmtukardari = models.DateTimeField(blank=True, null=True)
    pmtukarsampai = models.DateTimeField(blank=True, null=True)
    ppotberlaku = models.IntegerField(blank=True, null=True)
    mnote1 = models.CharField(max_length=255, blank=True, null=True)
    mnote2 = models.CharField(max_length=255, blank=True, null=True)
    pumumnopoin = models.BooleanField(blank=True, null=True)
    pmdapatdari = models.DateTimeField(blank=True, null=True)
    pmdapatsampai = models.DateTimeField(blank=True, null=True)
    mnote3 = models.CharField(max_length=255, blank=True, null=True)
    ppointopot = models.BooleanField(blank=True, null=True)
    mnote4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_settingpel'


class TblSupel(models.Model):
    kode = models.CharField(primary_key=True, max_length=50)
    tipe = models.CharField(max_length=2)
    nama = models.CharField(max_length=150, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    kota = models.CharField(max_length=100, blank=True, null=True)
    provinsi = models.CharField(max_length=100, blank=True, null=True)
    kodepos = models.CharField(max_length=20, blank=True, null=True)
    negara = models.CharField(max_length=100, blank=True, null=True)
    telepon = models.CharField(max_length=200, blank=True, null=True)
    fax = models.CharField(max_length=200, blank=True, null=True)
    kontak = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    norek = models.CharField(max_length=100, blank=True, null=True)
    atasnama = models.CharField(max_length=100, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    limitjmlhupi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    limitharihupi = models.IntegerField(blank=True, null=True)
    tipepot = models.CharField(max_length=5, blank=True, null=True)
    kgrup = models.CharField(max_length=20, blank=True, null=True)
    pilkomisi = models.IntegerField(blank=True, null=True)
    piljmlkomisi = models.IntegerField(blank=True, null=True)
    komisipr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisinom = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    npwp = models.CharField(max_length=100, blank=True, null=True)
    harijt = models.IntegerField(blank=True, null=True)
    kdwilayah = models.ForeignKey('TblSupelWil', models.DO_NOTHING, db_column='kdwilayah', blank=True, null=True)
    kdsubwil = models.ForeignKey('TblSupelSubwil', models.DO_NOTHING, db_column='kdsubwil', blank=True, null=True)
    kdsales = models.CharField(max_length=50, blank=True, null=True)
    maxjmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    syspajak = models.CharField(max_length=10, blank=True, null=True)
    opsyspajak = models.CharField(max_length=10, blank=True, null=True)
    nompajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nik = models.CharField(max_length=50, blank=True, null=True)
    nama_npwp = models.CharField(max_length=150, blank=True, null=True)
    alamat_npwp = models.TextField(blank=True, null=True)
    tgl_lahir = models.DateTimeField(blank=True, null=True)
    opsikredit = models.CharField(max_length=5, blank=True, null=True)
    acc_kredit = models.CharField(max_length=30, blank=True, null=True)
    stsaktif = models.CharField(max_length=15, blank=True, null=True)
    cekbglunas = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supel'
        unique_together = (('kode', 'tipe'),)


class TblSupelSubwil(models.Model):
    kode = models.CharField(primary_key=True, max_length=50)
    subwilayah = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supel_subwil'


class TblSupelWil(models.Model):
    kode = models.CharField(primary_key=True, max_length=50)
    wilayah = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supel_wil'


class TblSupelgrup(models.Model):
    kgrup = models.CharField(primary_key=True, max_length=20)
    grup = models.CharField(max_length=100, blank=True, null=True)
    potongan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    levelharga = models.IntegerField(blank=True, null=True)
    kelipatanpoin = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supelgrup'


class TblTagihandt(models.Model):
    iddetail = models.CharField(max_length=100, blank=True, null=True)
    notransaksi = models.CharField(max_length=200, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    idko_dt = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagihandt'


class TblTagihikdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblTagihikhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jumlah = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlpesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan2 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan3 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    potongan4 = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrmasuk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlrkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlsisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsibayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    idorder = models.CharField(max_length=150, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    idtrskonsinyasi = models.CharField(max_length=150, blank=True, null=True)
    jmlretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    notrskonsinyasi = models.CharField(max_length=100, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=50, decimal_places=3, blank=True, null=True)
    iddetailtrs = models.CharField(max_length=150, blank=True, null=True)
    xx = models.IntegerField(blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagihikdt'


class TblTagihikhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantordari = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kantordari', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notrsorder = models.CharField(max_length=50, blank=True, null=True)
    kodesupel = models.ForeignKey(TblSupel, models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    kodesales = models.CharField(max_length=50, blank=True, null=True)
    kodesales2 = models.CharField(max_length=50, blank=True, null=True)
    kodesales3 = models.CharField(max_length=50, blank=True, null=True)
    kodesales4 = models.CharField(max_length=50, blank=True, null=True)
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitempesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    prpajak = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    carabayar = models.CharField(max_length=20, blank=True, null=True)
    jmltunai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmldebit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkk = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi1 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi2 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi3 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    komisi4 = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    point_ik = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    point_sts = models.IntegerField(blank=True, null=True)
    nofp = models.CharField(max_length=100, blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    notrsretur = models.ForeignKey('self', models.DO_NOTHING, db_column='notrsretur', blank=True, null=True)
    acc_potongan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_potongan', blank=True, null=True)
    acc_pajak = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_pajak', blank=True, null=True)
    acc_biayalain = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_biayalain', blank=True, null=True)
    acc_tunai = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_tunai', blank=True, null=True)
    acc_kredit = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_kredit', blank=True, null=True)
    acc_sales = models.CharField(max_length=30, blank=True, null=True)
    acc_hpp = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_debit = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_debit', blank=True, null=True)
    acc_kk = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_kk', blank=True, null=True)
    acc_dppesanan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_biaya_pot = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    byr_krd_no = models.CharField(max_length=30, blank=True, null=True)
    byr_debit_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_debit_bank', blank=True, null=True)
    byr_kk_bank = models.ForeignKey(TblBank, models.DO_NOTHING, db_column='byr_kk_bank', blank=True, null=True)
    byr_debit_no = models.CharField(max_length=100, blank=True, null=True)
    byr_kk_no = models.CharField(max_length=100, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    tanggal_sa = models.DateField(blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    byr_komisi1 = models.BooleanField(blank=True, null=True)
    byr_komisi2 = models.BooleanField(blank=True, null=True)
    byr_komisi3 = models.BooleanField(blank=True, null=True)
    byr_komisi4 = models.BooleanField(blank=True, null=True)
    point_notrans = models.CharField(max_length=50, blank=True, null=True)
    notransaksi_ko = models.ForeignKey(TblIkhd, models.DO_NOTHING, db_column='notransaksi_ko', blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagihikhd'


class TblTagihimdt(models.Model):
    iddetail = models.CharField(primary_key=True, max_length=150)
    nobaris = models.IntegerField(blank=True, null=True)
    notransaksi = models.ForeignKey('TblTagihimhd', models.DO_NOTHING, db_column='notransaksi', blank=True, null=True)
    kodeitem = models.ForeignKey(TblItem, models.DO_NOTHING, db_column='kodeitem', blank=True, null=True)
    jmlkonsi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsiretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    satuan = models.ForeignKey(TblItemsatuan, models.DO_NOTHING, db_column='satuan', blank=True, null=True)
    harga = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potongan = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmllaku = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlreturjual = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlsisa = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkonsibayar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    tglexp = models.DateTimeField(blank=True, null=True)
    idtrsretur = models.CharField(max_length=150, blank=True, null=True)
    kodeprod = models.CharField(max_length=100, blank=True, null=True)
    idorder = models.CharField(max_length=150, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    sakantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='sakantor', blank=True, null=True)
    detinfo = models.TextField(blank=True, null=True)
    pothutang = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    notrsretur = models.CharField(max_length=100, blank=True, null=True)
    jmlkonversi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    nom_pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkeluar = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagihimdt'


class TblTagihimhd(models.Model):
    notransaksi = models.CharField(primary_key=True, max_length=50)
    kodekantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kodekantor', blank=True, null=True)
    kantortujuan = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='kantortujuan', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    tipe = models.CharField(max_length=20, blank=True, null=True)
    notrsorder = models.CharField(max_length=50, blank=True, null=True)
    kodesupel = models.ForeignKey(TblSupel, models.DO_NOTHING, db_column='kodesupel', blank=True, null=True)
    matauang = models.ForeignKey(TblMatauang, models.DO_NOTHING, db_column='matauang', blank=True, null=True)
    rate = models.DecimalField(max_digits=35, decimal_places=20, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    totalitem = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalitempesan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    potfaktur = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    pajak = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    biayalain = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalakhir = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    carabayar = models.CharField(max_length=20, blank=True, null=True)
    jmltunai = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    jmlkredit = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    acc_potongan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_potongan', blank=True, null=True)
    acc_pajak = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_pajak', blank=True, null=True)
    acc_biayalain = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_biayalain', blank=True, null=True)
    acc_tunai = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_tunai', blank=True, null=True)
    acc_kredit = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_kredit', blank=True, null=True)
    acc_hpp = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_hpp', blank=True, null=True)
    acc_tagihan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_tagihan', blank=True, null=True)
    acc_dppesanan = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_dppesanan', blank=True, null=True)
    acc_biaya_pot = models.ForeignKey(TblPerkiraan, models.DO_NOTHING, db_column='acc_biaya_pot', blank=True, null=True)
    byr_krd_jt = models.DateTimeField(blank=True, null=True)
    byr_krd_no = models.CharField(max_length=30, blank=True, null=True)
    krd_jml_pot = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    krd_jml_byr = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    user1 = models.CharField(max_length=50, blank=True, null=True)
    user2 = models.CharField(max_length=50, blank=True, null=True)
    dateupd = models.DateTimeField(blank=True, null=True)
    tanggal_sa = models.DateField(blank=True, null=True)
    biaya_msk_total = models.BooleanField(blank=True, null=True)
    potnomfaktur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    compname = models.CharField(max_length=255, blank=True, null=True)
    shiftkerja = models.CharField(max_length=20, blank=True, null=True)
    prpajak = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    dppesanan = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    notrsretur = models.ForeignKey('self', models.DO_NOTHING, db_column='notrsretur', blank=True, null=True)
    ppn = models.CharField(max_length=30, blank=True, null=True)
    totallaku = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalretur = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    totalkonsinyasi = models.DecimalField(max_digits=20, decimal_places=3, blank=True, null=True)
    bc_trf_sts = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagihimhd'


class TblTmp(models.Model):
    cntprsjurnal = models.BigIntegerField(blank=True, null=True)
    cntlevelrep = models.IntegerField(blank=True, null=True)
    cntsortrep = models.IntegerField(blank=True, null=True)
    cnt_im = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tmp'


class TblUser(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    nama = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    tipe = models.CharField(max_length=5, blank=True, null=True)
    loginkantor = models.ForeignKey(TblKantor, models.DO_NOTHING, db_column='loginkantor', blank=True, null=True)
    kelompok = models.ForeignKey('TblUserg', models.DO_NOTHING, db_column='kelompok', blank=True, null=True)
    loginshift = models.BooleanField(blank=True, null=True)
    synchronized = models.BooleanField(blank=True, null=True)
    kodesales = models.CharField(max_length=50, blank=True, null=True)
    stslogin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblUserakses(models.Model):
    klpakses = models.ForeignKey('TblUserg', models.DO_NOTHING, db_column='klpakses', blank=True, null=True)
    modulid = models.CharField(max_length=50, blank=True, null=True)
    mopen = models.BooleanField(blank=True, null=True)
    mnew = models.BooleanField(blank=True, null=True)
    medit = models.BooleanField(blank=True, null=True)
    mdel = models.BooleanField(blank=True, null=True)
    mlock = models.BooleanField(blank=True, null=True)
    urut = models.IntegerField(blank=True, null=True)
    kelompok = models.IntegerField(blank=True, null=True)
    mlocktgl = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_userakses'


class TblUsercusAcc(models.Model):
    klpakses = models.ForeignKey('TblUserg', models.DO_NOTHING, db_column='klpakses', blank=True, null=True)
    modulid = models.CharField(max_length=50, blank=True, null=True)
    customacc = models.CharField(max_length=50, blank=True, null=True)
    customval = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_usercus_acc'


class TblUserg(models.Model):
    kelompok = models.CharField(primary_key=True, max_length=30)
    urut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_userg'
