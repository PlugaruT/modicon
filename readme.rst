Overview
--------

Python library for getting readings from Modicon TM251 logic controller,
via Modbus, over a serial port.

Installation
^^^^^^^^^^^^

::

        pip install git+ssh://git@github.com/PlugaruT/modicon.git

Example of use
^^^^^^^^^^^^^^

Reading int, float values from register:

::

        from modicon import Modicon
        m = Modicon()

        result = m.read_register_value('OUT_POZITIE_MV3_1') # register name as parameter
        print(result)

Reading specific bit state:

::

        from modicon import Modicon
        m = Modicon()

        result = m.get_bit_state('TENSIUNE_UPS') # bit name as parameter
        print(result)

Reading all bit states from all registers:

::

        from modicon import Modicon
        m = Modicon()
        result = m.get_all_bits_state()
        print(result)

Reading bit states from specific register:

::

        from modicon import Modicon
        m = Modicon()

        result = m.get_bits_states_from_reg('ALARME_DWORD_4') # register name as parameter
        print(result)

References
^^^^^^^^^^

-  http://pymodbus.readthedocs.org/en/latest/library/sync-client.html -
   examples of Modbus clients
