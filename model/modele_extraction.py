# -*- coding:utf-8-*-


from extraction import CourrierInternational, LePoint, JournalduNet, LesEchos, LeDauphine, LaTribune, SudOuest, LeFigaro, LeParisien, _20minutes

def extraction_all():
        _20minutes.unes('http://www.20minutes.fr')
        CourrierInternational.unes('http://www.courrierinternational.com')
        JournalduNet.unes('http://www.lejournaldunet.fr')
        LaTribune.unes('http://www.latribune.fr')
        LeDauphine.unes('http://www.ledauphine.com')
        LeFigaro.unes('http://www.lefigaro.fr')
        LeParisien.unes('http://www.leparisien.fr')
        LePoint.unes('http://www.lepoint.fr')
        SudOuest.unes('http://www.sudouest.fr')
        return True



if __name__ == '__main__':
	print True



