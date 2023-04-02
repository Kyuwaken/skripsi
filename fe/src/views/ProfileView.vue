<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>
                        User Information
                    </v-card-title>
                    <v-card-text>
                        Name :
                    </v-card-text>
                    <v-card-text>
                        Phone :
                    </v-card-text>
                    <v-card-text>
                        Email :
                    </v-card-text>
                    <v-card-text>
                        NIK :
                    </v-card-text>
                    <v-card-actions class="justify-end">
                        <v-btn variant="outlined">
                            Update
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>


    </v-container>
</template>
  
<script>

export default {
    name: 'Profile',
    data() {
        return {
            name: '',
            phone: '',
            email: '',
            photo: '',
            nik: '',
            profile_picture: '',
        }
    },
    created() {
        // load user data
        axios.get('/api/profile').then(response => {
            this.name = response.data.name
            this.phone = response.data.phone
            this.email = response.data.email
            this.photo = response.data.photo
            this.nik = response.data.nik
            this.profile_picture = response.data.profile_picture
        })
    },
    methods: {
        saveProfile() {
            // send data to server to save
            axios.post('/api/profile', {
                name: this.name,
                phone: this.phone,
                email: this.email,
                photo: this.photo,
                nik: this.nik,
            }).then(response => {
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
  
<style>
h1 {
    margin: 0;
    font-size: 36px;
}
</style>