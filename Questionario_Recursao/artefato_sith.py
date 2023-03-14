from _typeshed import NoneType


def buscarArtefato():
    if bb8.verificarChao():
        return bb8.verificarChao()
    else:
        bb8.registrarComoVisitado()
        artefato = False
        if not artefato and bb8.verificarNorte():
            bb8.moverNorte()
            if not bb8.verificarSeFoiVisitado():
                artefato = buscarArtefato()
            if not artefato:
                bb8.moverSul()
        
        if not artefato and bb8.verificarLeste():
            bb8.moverLeste()
            if  not bb8.verificarSeFoiVisitado():
                artefato = buscarArtefato()
            if not artefato:
                bb8.moverOeste()

        if not artefato and bb8.verificarOeste():
            bb8.moverOeste()
            if not bb8.verificarSeFoiVisitado():
                artefato = buscarArtefato()
            if not artefato:
                bb8.moverLeste()

        if not artefato and bb8.verificarSul():
            bb8.moverSul()
            if not bb8.verificarSeFoiVisitado():
                artefato = buscarArtefato()
            if not artefato:
                bb8.moverNorte()
        return artefato
