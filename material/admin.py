from django.contrib import admin
from nested_admin import nested
from .models import *

class UcInline(admin.StackedInline):
    model = UC
    classes = ['collapse']
    extra = 1

class MoniteurInline(admin.StackedInline):
    model = Moniteur
    classes = ['collapse']
    extra = 1

class ClavierInline(admin.StackedInline):
    model = Clavier
    classes = ['collapse']
    extra = 1

class SourisInline(admin.StackedInline):
    model = Souris
    classes = ['collapse']
    extra = 1

class HautParleurInline(admin.StackedInline):
    model = HautParleur
    classes = ['collapse']
    extra = 1

    
@admin.register(OrdinateurDeBureau)
class OrdinateurDeBureauAdmin(admin.ModelAdmin):
    inlines = [UcInline,MoniteurInline,ClavierInline,SourisInline,HautParleurInline]

class OrdinateurInline(admin.StackedInline):
    model = Ordinateur
    classes = ['collapse']
    extra = 1

class ChargeurInline(admin.StackedInline):
    model = Chargeur
    classes = ['collapse']
    extra = 1
    
@admin.register(OrdinateurPortable)
class OrdinateurPortableAdmin(admin.ModelAdmin):
    inlines = [ChargeurInline,OrdinateurInline]
    
class ServeurInline(admin.StackedInline):
    model = Serveur
    classes = ['collapse']
    extra = 1

class BaieStockageInline(admin.StackedInline):
    model = BaieStockage
    classes = ['collapse']
    extra = 1

class DisqueDurSSDInline(admin.StackedInline):
    model = DisqueDurSSD
    classes = ['collapse']
    extra = 1
    
class MemoireRAMServeurInline(admin.StackedInline):
    model =MemoireRAMServeur
    classes = ['collapse']
    extra = 1
    
class ProcesseurServeurInline(admin.StackedInline):
    model = ProcesseurServeur
    classes = ['collapse']
    extra = 1
     
@admin.register(Serveurs)
class ServeurAdmin(admin.ModelAdmin):
    inlines = [ServeurInline,BaieStockageInline,DisqueDurSSDInline,MemoireRAMServeurInline,ProcesseurServeurInline]
    
class RouteurInline(admin.StackedInline):
    model = Routeur
    extra = 1

class CommutateurInline(admin.StackedInline):
    model = Commutateur
    extra = 1

class PareFeuInline(admin.StackedInline):
    model = PareFeu
    extra = 1

class PointAccesSansFilInline(admin.StackedInline):
    model = PointAccesSansFil
    extra = 1

@admin.register(Réseau)
class RéseauAdmin(admin.ModelAdmin):
    inlines = [RouteurInline, CommutateurInline, PareFeuInline, PointAccesSansFilInline]    
    
class DisqueDurExterneInline(admin.StackedInline):
    model = DisqueDurExterne
    extra = 1

class CleUSBInline(admin.StackedInline):
    model = CleUSB
    extra = 1

class CarteMemoireInline(admin.StackedInline):
    model = CarteMemoire
    extra = 1

class LecteurDisqueOptiqueInline(admin.StackedInline):
    model = LecteurDisqueOptique
    extra = 1

@admin.register(PériphériquesDeStockage)
class PériphériquesDeStockageAdmin(admin.ModelAdmin):
    inlines = [DisqueDurExterneInline, CleUSBInline, CarteMemoireInline, LecteurDisqueOptiqueInline]
    
class ImprimanteInline(admin.StackedInline):
    model = Imprimante
    extra = 1

class ScannerInline(admin.StackedInline):
    model = Scanner
    extra = 1

@admin.register(ImprimantesEtScanners)
class ImprimantesEtScannersAdmin(admin.ModelAdmin):
    inlines = [ImprimanteInline, ScannerInline]

class SauvegardeSurBandeInline(admin.StackedInline):
    model = SauvegardeSurBande
    extra = 1

class SauvegardeSurDisqueInline(admin.StackedInline):
    model = SauvegardeSurDisque
    extra = 1

class AlimentationSansInterruptionInline(admin.StackedInline):
    model = AlimentationSansInterruption
    extra = 1

class SurveillanceReseauSecuriteInline(admin.StackedInline):
    model = SurveillanceReseauSecurite
    extra = 1

@admin.register(EquipementDeSauvegardeEtDeSecurite)
class EquipementDeSauvegardeEtDeSecuriteAdmin(admin.ModelAdmin):
    inlines = [SauvegardeSurBandeInline, SauvegardeSurDisqueInline, AlimentationSansInterruptionInline, SurveillanceReseauSecuriteInline]
    
class CableEthernetInline(admin.StackedInline):
    model = CableEthernet
    extra = 1

class CableUSBInline(admin.StackedInline):
    model = CableUSB
    extra = 1

class AdaptateurInline(admin.StackedInline):
    model = Adaptateur
    extra = 1

class ConnecteurInline(admin.StackedInline):
    model = Connecteur
    extra = 1

@admin.register(Accessoires)
class AccessoiresAdmin(admin.ModelAdmin):
    inlines = [CableEthernetInline, CableUSBInline, AdaptateurInline, ConnecteurInline]
    
class ProjecteurInline(admin.StackedInline):
    model = Projecteur
    extra = 1

class EcranInteractifInline(admin.StackedInline):
    model = EcranInteractif
    extra = 1

@admin.register(AccessoiresDePresentation)
class AccessoiresDePresentationAdmin(admin.ModelAdmin):
    inlines = [ProjecteurInline, EcranInteractifInline]
    
class CameraVideosurveillanceInline(admin.StackedInline):
    model = CameraVideosurveillance
    extra = 1

class SystemeConferenceAudiovisuelleInline(admin.StackedInline):
    model = SystemeConferenceAudiovisuelle
    extra = 1

@admin.register(MaterielAudiovisuel)
class MaterielAudiovisuelAdmin(admin.ModelAdmin):
    inlines = [CameraVideosurveillanceInline, SystemeConferenceAudiovisuelleInline]
    
class TabletteInline(admin.StackedInline):
    model = Tablette
    extra = 1

class SmartphoneEntrepriseInline(admin.StackedInline):
    model = SmartphoneEntreprise
    extra = 1

class AccessoireMobileInline(admin.StackedInline):
    model = AccessoireMobile
    extra = 1

@admin.register(Mobilite)
class MobiliteAdmin(admin.ModelAdmin):
    inlines = [TabletteInline, SmartphoneEntrepriseInline, AccessoireMobileInline]
    
class VentilateurBoitierInline(admin.StackedInline):
    model = VentilateurBoitier
    extra = 1

class SystemeRefroidissementLiquideInline(admin.StackedInline):
    model = SystemeRefroidissementLiquide
    extra = 1

@admin.register(SystemesDeRefroidissement)
class SystemesDeRefroidissementAdmin(admin.ModelAdmin):
    inlines = [VentilateurBoitierInline, SystemeRefroidissementLiquideInline]
    
class SystemeExploitationInline(admin.StackedInline):
    model = SystemeExploitation
    extra = 1

class LogicielProductiviteInline(admin.StackedInline):
    model = LogicielProductivite
    extra = 1

class LogicielCRMInline(admin.StackedInline):
    model = LogicielCRM
    extra = 1

class LogicielCollaborationInline(admin.StackedInline):
    model = LogicielCollaboration
    extra = 1

class SolutionSauvegardeInline(admin.StackedInline):
    model = SolutionSauvegarde
    extra = 1

class LogicielSecuriteInline(admin.StackedInline):
    model = LogicielSecurite
    extra = 1

class LogicielComptaFinanceInline(admin.StackedInline):
    model = LogicielComptaFinance
    extra = 1

class SolutionITSMInline(admin.StackedInline):
    model = SolutionITSM
    extra = 1

@admin.register(Logiciel)
class LogicielAdmin(admin.ModelAdmin):
    inlines = [SystemeExploitationInline, LogicielProductiviteInline, LogicielCRMInline,
               LogicielCollaborationInline, SolutionSauvegardeInline, LogicielSecuriteInline,
               LogicielComptaFinanceInline, SolutionITSMInline]