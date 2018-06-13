# Visual_geprom

Visual geprom è un programma per la gestione multipla di postazioni video.
Dalla finestra principale è possibile inserire i dati di accesso per l' amministrazione dei dispositivi, prima operazione necessaria
per poter utilizzare le successive funzionalità dell' applicazione.
Al di sotto della sezione dedicata all' accesso sono presenti dei pulsanti per il controllo delle presentazione di immagini (start e stop) e delle presentazioni di video (start video e stop video). Premendo uno di questi pulsanti viene inviato tramite una connessione tcp criptata in aes un comando al server che permette di avviare la presentazione selezionata.
È possibile gestire una postazione video precedentemente configurata selezionandolo dalla lista presente sul lato sinistro dello
schermo. In caso si vogla controllare una postazione nuova o non configurata è possibile inserire manualmente i dati relativi al
dispositivo ed in caso di necessità salvarlo nella propria lista inserendo l' indirizzo ip e la porta negli appositi spazi presenti sulla destra della lista di schermi già configurati. Da qui è possibile aggiungere il dispositivo alla propria lista oppure selezionarlo senza salvarlo.
Sopra la lista di schermi salvati è presente un pulsante 'verify', che permette di visualizzare a video l' indirizzo e la porta dello schermo selezionato.
sopra la sezione dedicata all' inserimento dei dati relativi ai dispositivi non salvati è presente il pulsante 'show file', che permette di aprire la finestra dedicata alla gestione dei file presenti sul disposistivo selezionato.
Questa finestra permette di visualizzare i file presenti separandoli fra attivi e non attivi. è possibile spostare i file da una condizione all' altra, eliminarli definitivamente oppure caricare un file o il contenuto di una cartella. I nuovi file caricati vengono automaticamente constrassegnati come inattivi. 
