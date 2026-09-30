# ProGuard rules for SIIPOL Jefatura

-keep class com.getcapacitor.** { *; }
-keep class com.ven911zulia.siipol.** { *; }
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keepattributes *Annotation*
-keepattributes JavascriptInterface
-keepattributes SourceFile,LineNumberTable
