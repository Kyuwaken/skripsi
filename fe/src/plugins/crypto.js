import AES from 'crypto-js/aes';
import Base64 from 'crypto-js/enc-base64';
import CryptoJS from 'crypto-js';

const key = '6c33d4abde09fe1c4ac9b76f245d7df4'
const iv = 'ddc5b6c4d6e4b6c4'
export default {
    methods: {
        encryptData(data) {
            var keys = CryptoJS.enc.Utf8.parse(key);
            var ivs = CryptoJS.enc.Utf8.parse(iv);
            var encrypted = CryptoJS.AES.encrypt(data, keys, { iv: ivs, mode: CryptoJS.mode.CBC});
            var text = encrypted.toString()
            return text;
        },
        decryptData(encryptedData) {
            var keys = CryptoJS.enc.Utf8.parse(key); 
            var ivs = CryptoJS.enc.Utf8.parse(iv)
            var decrypted =  CryptoJS.AES.decrypt(encryptedData, keys, { iv: ivs, mode: CryptoJS.mode.CBC});
            return decrypted.toString(CryptoJS.enc.Utf8)
        },
        encryptLocalStorage(data){
            const json = JSON.stringify(data)
            const encrypted = CryptoJS.AES.encrypt(json, key, {
                iv: iv,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            })
            return encrypted.toString()
        },
        decryptLocalStorage(encryptedData) {
            const decrypted = CryptoJS.AES.decrypt(encryptedData, key, {
              iv: iv,
              mode: CryptoJS.mode.CBC,
              padding: CryptoJS.pad.Pkcs7
            })
            const json = decrypted.toString(CryptoJS.enc.Utf8)
            return JSON.parse(json)
        },
        // encryptDataToken(data){
        //     const json = JSON.stringify(data)
        //     const encrypted = CryptoJS.AES.encrypt(json, key, {
        //         iv: iv,
        //         mode: CryptoJS.mode.CBC
        //     })
        //     return encrypted.toString()
        // },
        encryptDataToken(data){
            const json = JSON.stringify(data)
            var keys = CryptoJS.enc.Utf8.parse(key);
            var ivs = CryptoJS.enc.Utf8.parse(iv);
            var encrypted = CryptoJS.AES.encrypt(json, keys, { iv: ivs, mode: CryptoJS.mode.CBC});
            var text = encrypted.toString()
            return text;
        }
    }
}