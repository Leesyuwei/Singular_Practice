@echo off
java -Xmx5G -Xms2G -server ^
-XX:ParallelGCThreads=4 ^
-Xincgc -XX:+UseConcMarkSweepGC ^
-XX:+UseParNewGC ^
-XX:+CMSIncrementalPacing ^
-XX:+CMSParallelRemarkEnabled ^
-XX:+DisableExplicitGC ^
-XX:+UseAdaptiveGCBoundary ^
-XX:-UseGCOverheadLimit ^
-XX:+UseBiasedLocking ^
-XX:+UseLargePages ^
-Xnoclassgc ^
-XX:+OptimizeStringConcat ^
-XX:+UseFastAccessorMethods ^
-XX:+AggressiveOpts ^
-XX:MaxGCPauseMillis=50 ^
-XX:SurvivorRatio=8 ^
-XX:TargetSurvivorRatio=90 ^
-XX:MaxTenuringThreshold=15 ^
-XX:UseSSE=3 ^
-XX:PermSize=128m ^
-XX:LargePageSizeInBytes=4m ^
-jar server.jar
pause