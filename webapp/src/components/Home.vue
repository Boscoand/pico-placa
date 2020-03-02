<template>
  <v-card
    class="mt-10 mx-auto"
    outlined
  >
    <v-list-item three-line>

      <v-list-item-content>
        <!-- Title -->
        <v-list-item-title class="headline mt-4 mb-10">Predictor de Pico y Placa</v-list-item-title>
        <v-text-field
            v-model="license_plate"
            :rules="rules"
            :counter="7"
            label="Ingrese la placa de su vehículo"
        ></v-text-field>

        <v-row>

          <!-- Date Picker -->
          <v-col cols="12" sm="6">
            <v-menu
              ref="date_menu"
              v-model="date_activator"
              :close-on-content-click="false"
              :return-value.sync="date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="date"
                  label="Fecha"
                  prepend-icon="event"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="date_menu = false">Cancelar</v-btn>
                <v-btn text color="primary" @click="$refs.date_menu.save(date)">OK</v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>

          <!-- Time Picker -->
          <v-col cols="12" sm="6">
            <v-menu
              ref="time_menu"
              v-model="time_activator"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="time"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="time"
                  label="Hora"
                  prepend-icon="access_time"
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="time_activator"
                v-model="time"
                full-width
                @click:minute="$refs.time_menu.save(time)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>

      </v-list-item-content>
    </v-list-item>

    <!-- Execute Query -->
    <v-card-actions>
      <v-btn tile color="primary" dark v-on:click="query" class="mb-5">CONSULTAR</v-btn>
    </v-card-actions>

    <!-- Alerts -->
    <v-alert type="success" class="ml-2 mr-2" v-show="show_success_alert">
      Su vehículo sí puede circular el {{date}} a las {{time}}.
    </v-alert>

    <v-alert type="error" class="ml-2 mr-2" v-show="show_error_alert">
      Su vehículo no puede circular el {{date}} a las {{time}}.
    </v-alert>

    <v-alert type="error" class="ml-2 mr-2" v-show="show_empty_field_error">
      Llene todos los campos correctamente.
    </v-alert>

  </v-card>
</template>

<script>

import axios from 'axios'

export default {

  data () {
    return {
      show_success_alert: false,
      show_error_alert: false,
      show_empty_field_error: false,
      pattern: /^[A-Za-z]{3}\d{4}$/,
      rules: [
        value => !!value || 'Requerido.',
        value => (value || '').length <= 7 || 'Máximo 7 caracteres',
        value => {
          return this.pattern.test(value) || 'Placa inválida. La placa debe poseer el siguiente formato: XXX0123'
        }
      ],
      license_plate: null,
      date: null,
      date_activator: false,
      date_menu: false,
      time: null,
      time_activator: false,
      time_menu: false
    }
  },

  methods: {

    query () {
      this.show_success_alert = false
      this.show_error_alert = false

      if (!this.pattern.test(this.license_plate) || this.date == null || this.time == null) {
        this.show_empty_field_error = true
      } else {
        const params = '?license_plate=' + this.license_plate + '&date=' + this.date + '&time=' + this.time
        const path = 'http://localhost:5000/api/query' + params

        axios.get(path).then((response) => {
          response.data.available ? (this.show_success_alert = true) : (this.show_error_alert = true)
        }).catch((error) => {
          console.log(error)
        })
        this.show_empty_field_error = false
      }
    }

  }

}

</script>
