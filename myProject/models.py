from django.db import models
from django.conf import settings
from django.utils import timezone
from .generaCodice import genera
from myProject.utils import sendTransaction
import json
import hashlib

class Diploma(models.Model):
    tipologia = models.CharField(max_length= 30)
    nome = models.CharField(max_length= 20)
    cognome = models.CharField(max_length= 20)
    dataNascita = models.DateField()
    luogoNascita = models.CharField(max_length= 30)
    dataConseguimento = models.DateField(default= timezone.now)
    votazione = models.IntegerField()
    codiceId = models.CharField(max_length= 20, blank= True, null= True)
    hash = models.CharField(max_length= 64, default= None, blank= True, null= True)
    txId = models.CharField(max_length= 66, default= None, blank= True, null= True)

    def registra(self):
        self.codiceId = genera()
        data = {
            'tipologia': self.tipologia,
            'nome': self.nome,
            'cognome': self.cognome,
            'dataNascita': str(self.dataNascita),
            'luogoNascita': self.luogoNascita,
            'dataConseguimento': str(self.dataConseguimento),
            'votazione': self.votazione,
            'codiceId': self.codiceId
        }
        dtj = json.dumps(data)
        sha256_hash = hashlib.new('SHA256')
        sha256_hash.update(dtj.encode())
        self.hash = sha256_hash.hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

    def __str__(self):
        nominativo = f'{self.nome} {self.cognome}'
        return nominativo