# Log parser


## Log Descriptors  
  
  
### POET  
#### Cheat Sheet  
_If a key has is described multiple times it can be explained as multiple ways._  
  
| Key  | Description  |
|------|--------------|
| HB_NUM  | The heartbeat used when this poet apply was activated.  |
| HB_RATE  | The current ```Window Heartbeat Rate```. Can check the ```Heartbeat``` with ```Tag``` equal to ```HB_NUM```.  |
| X_HAT_MINUS  |The previous _`X_HAT`_.  |
| X_HAT  | NONE |
| P_MINUS  | Previous _`P`_ plus 0.00001.  |
| H  | The `Speedup` from the previous poet apply.  |
| K  | Seems to be **Kalman** specific.  |
| P  | NONE |
| SPEEDUP  | The new _`Speedup`_ to apply.  |
| ERROR  | Difference between wanted ```HB_RATE``` (MAX window size - MIN window size) and gotten ```HB_RATE``` |
| WORKLOAD  | Estimate of the performance workload  |
| WORKLOAD  | Estimate of time between heartbeats given minimum amount of resources |
| LOWER_ID  | Poet sets to configurations each apply. This is the _`Id`_ of config with lowest speedup changed to this round.  |
| UPPER_ID  | _`Id`_ of config with highest speedup changed to after this round.  |
| NUM_HBS  | The number of heartbeats spent in lower configuration. 0 if lower_id == upper_id.  |
  
  
_NOTE: Setting the pole as described in the poet paper can be done in the poet/src/poet_constands.h file, by setting `FAST`, `SLOW` or neither. If neither is set, it uses a pole of zero (0) as default. Changing **P1** changes the pole as described in the poet paper. The other variables are for using poet in a more advanced way._  
_NOTE: A small `pole` means that the `poet` is more reactive. Zero (0) is unmitigated, while One (1) is rigid._  
_NOTE: When using only one pole, as is described in the poet paper, in the poet implementation provided, speedup can be calculated as: ```SPEEDUP = H + 'pole' * WORKLOAD * ERROR```_  
_NOTE: See more in paper:_  
1. _https://ieeexplore.ieee.org/document/7108419/._  
2. _Docs/poet.pdf_  
  
### Heartbeat  
_For More information check your documentation folder_  
#### Cheat Sheet  
  
| Key  | Description  |
|------|--------------|
|  Beat  | Incrementing counter for each time heartbeat has been called |
|  Tag  | Index for loggin of heartbeat. Increases for each heartbeat log |
|  Timestamp  | Time when current heartbeat happened. On unix systems the time is given as nanosecond timestamps. See **python** ```time.time()``` |
|  Global_Rate  | Average rate of `heartbeats` per second from first timestamp |
|  Global_Rate  | Returns the heart rate over the life of the entire application |
|  Window_Rate  | Used by `POET` |
|  Window_Rate  | Average rate of `heartbeats` per second this window |
|  Window_Rate  | Returns the heart rate over the last window (as specified to init) |
|  Instant_Rate  | The rate of `heartbeats` per second this if one only takes a look at the current heartbeat and its predecessor taking only this `heartbeat` and its predecessor into consideration |
|  Instant_Rate  |Returns the heart rate for the last heartbeat. |
|  Global_Accuracy  | NONE |
|  Window_Accuracy  | NONE |
|  Instant_Accuracy  | NONE |
|  Global_Power  | Total power from the first `heartbeat` to the current `heartbeat tag` |
|  Global_Power  | The power (double) over the entire life of the application |
|  Window_Power  | Used by `POET` |
|  Window_Power  | The power (double) over the last window |
|  Instant_Power   | The power (double) for the last heartbeat |
  
_NOTE: Information regarding `Power` description has been collected from `heartbeats/inc/heartbeat-accuracy-power.h` and `heartbeats/src/heartbeat-accuracy-power-shared.c`  
#### Documentation creation  
_Documentation stored as ```refman.pdf```_.  
_Note: Field descriptions are usless/non-existent_.  
1. Go into your ```hearbeats``` folder.
2. Run ```doxygen heartbeats_doc```.
3. Go into latex documentation folder for heartbeat: ```cd cd doc/latex```.
4. Run make: ```make```.
File is now stored as _```refman.pdf```_.  
  
## Kelman filter  
_```Kalman filtering, also known as linear quadratic estimation (LQE), is an algorithm that uses a series of measurements observed over time, containing statistical noise and other inaccuracies, and produces estimates of unknown variables that tend to be more accurate than those based on a single measurement alone, by estimating a joint probability distribution over the variables for each timeframe. The filter is named after Rudolf E. Kálmán, one of the primary developers of its theory.```_  
**From** _https://en.wikipedia.org/wiki/Kalman_filter_  
  
