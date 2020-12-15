axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue ({
    el: '#app',
    data: {
        api: '/api/events?format=json',
        events: []
    },
    
    created: function () {
        const vue = this;
        axios.get(vue.api)
        .then((response) => {
            vue.events = response.data
        })
        .catch((error) => {
            console.log('Failed')
        })
    },
    methods: {
        removeItem (idx) {
            this.events.splice(idx, 1)
            const vue = this;
            axios.post('api/events/' + idx + '', {event: vue.events})
            .then(() => {
                console.log('успех')
            })
        }
    }
})