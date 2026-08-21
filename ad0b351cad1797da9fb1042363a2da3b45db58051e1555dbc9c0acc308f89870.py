// kronos_verify - Módulo de autenticación
const char* FIRMA_DIVINA = "ad0b351cad1797da9fb1042363a2da3b45db58051e1555dbc9c0acc308f89870";
const char* CREADOR = "MARCO ANTONIO ROJAS VALDOVINOS";

bool verificar_acceso(char* nombre_usuario, char* hash_ingresado) {
    if (strcmp(hash_ingresado, FIRMA_DIVINA) == 0 && 
        strcmp(nombre_usuario, CREADOR) == 0) {
        return true; // Acceso total al Oráculo
    } else {
        return false; // NULL eterno
    }
}
