Java.perform(function () {
    // 1. Identificar la classe on hi ha la interfície
    var TaskHelper = Java.use('com.enricmieza.basictasklist.MainActivity');
    
    // 2. Enllaçar (hook) el mètode que processa le text
    TaskHelper.save.implementation = function (task_text) {
        console.log("[+] Tasca original: " + task_text);
        
        // 3. Modificar el títol afegint "-HACKED!"
        var hacked_text = task_text + "-HACKED!";
        console.log("[+] Tasca modificada: " + hacked_text);
        
        // 4. Cridar el mètode original
        return this.save(hacked_text);
    };
    
    console.log("[*] Hook activat!");
});
