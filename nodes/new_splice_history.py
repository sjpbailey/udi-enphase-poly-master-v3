
"""def siteHist(self, command):
    presentday = datetime.now()
    yesterday = presentday - timedelta(1)
    start_date = yesterday.strftime('%Y-%m-%d')
    end_date = presentday.strftime('%Y-%m-%d')
    LOGGER.info(start_date)
    LOGGER.info(end_date)
     URL_HIST = 'https://api.enphaseenergy.com/api/v2/systems/2527105/energy_lifetime?start_date=' + \
          start_date+'&end_date=' + end_date
      params = (('key', self.key), ('user_id', self.user_id))

       try:
            r = requests.get(URL_HIST, params=params)
            #print('\n Summary \n' + response)
            Response = json.loads(r.text)

            LOGGER.info(Response)
            self.setDriver('GV5', float(Response/1000))

            # LOGGER.info(Response["current_power"])
            #self.setDriver('GV2', float(Response["energy_today"]/1000))
            # LOGGER.info(Response["current_power"])
            #self.setDriver('GV3', float(Response["energy_lifetime"]/1000))
            # LOGGER.info(Response["status"])
            #self.setDriver('GV4', str(Response["status"]))

            if r.status_code == 200:
                self.setDriver('ST', 1)
            else:
                self.setDriver('ST', 0)
        except requests.exceptions.RequestException as e:
            LOGGER.error("Error: " + str(e))"""
