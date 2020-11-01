# from datetime import date, time, datetime, timedelta
# from dateutil.tz import UTC, tzlocal, gettz, resolve_imaginary

# ### CONSTRUCTORS
# <D>  = date(year, month, day)
# <T>  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
# <DT> = datetime(year, month, day, hour=0, minute=0, second=0, ...)
# <TD> = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
#                  minutes=0, hours=0, weeks=0)


# ### NOW
# <D/DTn>  = D/DT.today()                     # Current local date or naive datetime.
# <DTn>    = DT.utcnow()                      # Naive datetime from current UTC time.
# <DTa>    = DT.now(<tzinfo>)                 # Aware datetime from current tz time.

# ### TIMEZONE
# <tzinfo> = UTC                              # UTC timezone. London without DST.
# <tzinfo> = tzlocal()                        # Local timezone. Also gettz().
# <tzinfo> = gettz('<Continent>/<City>')      # 'Continent/City_Name' timezone or None.
# <DTa>    = <DT>.astimezone(<tzinfo>)        # Datetime, converted to passed timezone.
# <Ta/DTa> = <T/DT>.replace(tzinfo=<tzinfo>)  # Unconverted object with new timezone.

# ### ENCODE
# <D/T/DT> = D/T/DT.fromisoformat('<iso>')    # Object from ISO string. Raises ValueError.
# <DT>     = DT.strptime(<str>, '<format>')   # Datetime from str, according to format.
# <D/DTn>  = D/DT.fromordinal(<int>)          # D/DTn from days since Christ, at midnight.
# <DTn>    = DT.fromtimestamp(<real>)         # Local time DTn from seconds since Epoch.
# <DTa>    = DT.fromtimestamp(<real>, <tz.>)  # Aware datetime from seconds since Epoch.

# ### DECODE
# <str>    = <D/T/DT>.isoformat(sep='T')      # Also timespec='auto/hours/minutes/seconds'.
# <str>    = <D/T/DT>.strftime('<format>')    # Custom string representation.
# <int>    = <D/DT>.toordinal()               # Days since Christ, ignoring time and tz.
# <float>  = <DTn>.timestamp()                # Seconds since Epoch, from DTn in local tz.
# <float>  = <DTa>.timestamp()                # Seconds since Epoch, from DTa.

# ### ARITHMETICS
# <D/DT>   = <D/DT>   ± <TD>                  # Returned datetime can fall into missing hour.
# <TD>     = <D/DTn>  - <D/DTn>               # Returns the difference, ignoring time jumps.
# <TD>     = <DTa>    - <DTa>                 # Ignores time jumps if they share tzinfo object.
# <TD>     = <DT_UTC> - <DT_UTC>              # Convert DTs to UTC to get the actual delta.

# ### ARGUMENTS
# # Inside Function Call
# <function>(<positional_args>)                  # f(0, 0)
# <function>(<keyword_args>)                     # f(x=0, y=0)
# <function>(<positional_args>, <keyword_args>)  # f(0, y=0)

# #Inside Function Definition
# def f(<nondefault_args>):                      # def f(x, y):
# def f(<default_args>):                         # def f(x=0, y=0):
# def f(<nondefault_args>, <default_args>):      # def f(x, y=0):
pass