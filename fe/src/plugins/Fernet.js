import fernet from "fernet";

// const ENCRYPT_SECRET =  new fernet.Secret(process.env.VUE_APP_BUDGETIN_KEY);
const ENCRYPT_SECRET =  new fernet.Secret('4aEZPz1CoUWbujbe-_lYERfZuV_bSatnFj4y_R2L1W0=');
export default {
    methods: {
/**
 * Function to encrypt plaintext to backend
 * @returns (string) ciphertext
 */
  encrypt(plaintext) {
    let token = new fernet.Token({
      secret: ENCRYPT_SECRET,
    });

    let ciphertext = token.encode(plaintext);
    return ciphertext;
  },
  /**
   * Function to decrypt ciphertext from backend
   * @returns (string) plaintext
   */
   decrypt(ciphertext) {
    let token = new fernet.Token({
      secret: DECRYPT_SECRET,
      token: ciphertext,
    });
    let plaintext = token.decode();
    return plaintext;
  }
// const _key = 'abcdefghijklmn'
//     const _password ='123456'

//     //encryption
//     console.log(this.encryptByDES(_password,_key))
//     //Decrypt
//     console.log(this.decryptByDES(_password,_key))

}}