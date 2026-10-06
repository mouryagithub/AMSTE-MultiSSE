; ModuleID = '/mnt/d/Major_Project/parrot/build/subprojects/ara/appl/AUTOSAR/autosar_multicore_minexample.pi4.ll'
source_filename = "../subprojects/ara/appl/AUTOSAR/multicore/minexample.cc"
target datalayout = "e-m:e-p:32:32-Fi8-i64:64-v128:64:128-a:0:32-n32-S64"
target triple = "thumbv7-none-unknown-eabi"

@AUTOSAR_TASK_TaskA = external dso_local constant i32, align 4
@AUTOSAR_TASK_TaskE = external dso_local constant i32, align 4
@.str = private unnamed_addr constant [5 x i8] c"DAFE\00", align 1
@trace_table_idx = external dso_local global i32, align 4
@experiment_number = external dso_local global i32, align 4
@global_all_ok = external dso_local global i8, align 1
@llvm.compiler.used = appending global [1 x i8*] [i8* bitcast (void ()* @AUTOSAR_ISR_Interrupt1 to i8*)], section "llvm.metadata"

; Function Attrs: alwaysinline mustprogress nounwind
define dso_local void @AUTOSAR_ISR_Interrupt1() #0 !dbg !32 {
entry:
  call void @test_trace(i8 noundef zeroext 49), !dbg !36
  ret void, !dbg !37
}

declare dso_local void @test_trace(i8 noundef zeroext) #1

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskA() #2 !dbg !38 {
entry:
  call void @test_trace(i8 noundef zeroext 65), !dbg !39
  %call = call i32 @AUTOSAR_TerminateTask(), !dbg !40
  ret void, !dbg !41
}

declare dso_local i32 @AUTOSAR_TerminateTask() #1

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskB() #2 !dbg !42 {
entry:
  call void @test_trace(i8 noundef zeroext 66), !dbg !43
  %call = call i32 @AUTOSAR_TerminateTask(), !dbg !44
  ret void, !dbg !45
}

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskC() #2 !dbg !46 {
entry:
  call void @test_trace(i8 noundef zeroext 67), !dbg !47
  %call = call i32 @AUTOSAR_TerminateTask(), !dbg !48
  ret void, !dbg !49
}

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskD() #2 !dbg !50 {
entry:
  call void @test_trace(i8 noundef zeroext 68), !dbg !51
  %0 = load i32, i32* @AUTOSAR_TASK_TaskA, align 4, !dbg !52
  %call = call i32 @AUTOSAR_ActivateTask(i32 noundef %0), !dbg !52
  %call1 = call i32 @AUTOSAR_TerminateTask(), !dbg !53
  ret void, !dbg !54
}

declare dso_local i32 @AUTOSAR_ActivateTask(i32 noundef) #1

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskE() #2 !dbg !55 {
entry:
  call void @test_trace(i8 noundef zeroext 69), !dbg !56
  call void @AUTOSAR_ShutdownAllCores(i32 noundef 0) #6, !dbg !57
  unreachable, !dbg !57
}

; Function Attrs: noreturn
declare dso_local void @AUTOSAR_ShutdownAllCores(i32 noundef) #3

; Function Attrs: mustprogress noinline nounwind
define dso_local void @AUTOSAR_TASK_FUNC_TaskF() #2 !dbg !58 {
entry:
  call void @test_trace(i8 noundef zeroext 70), !dbg !59
  %0 = load i32, i32* @AUTOSAR_TASK_TaskE, align 4, !dbg !60
  %call = call i32 @AUTOSAR_ActivateTask(i32 noundef %0), !dbg !60
  %call1 = call i32 @AUTOSAR_TerminateTask(), !dbg !61
  ret void, !dbg !62
}

; Function Attrs: mustprogress noinline nounwind
define dso_local void @_Z5startv() #2 !dbg !63 {
entry:
  %rv = alloca i32, align 4
  call void @llvm.dbg.declare(metadata i32* %rv, metadata !64, metadata !DIExpression()), !dbg !66
  %call = call i32 @AUTOSAR_GetCoreID(), !dbg !67
  switch i32 %call, label %sw.default [
    i32 0, label %sw.bb
  ], !dbg !68

sw.bb:                                            ; preds = %entry
  call void @AUTOSAR_StartCore(i32 noundef 1, i32* noundef %rv), !dbg !69
  br label %sw.default, !dbg !69

sw.default:                                       ; preds = %sw.bb, %entry
  call void @AUTOSAR_StartOS(i32 noundef 0), !dbg !71
  br label %sw.epilog, !dbg !72

sw.epilog:                                        ; preds = %sw.default
  ret void, !dbg !73
}

; Function Attrs: nofree nosync nounwind readnone speculatable willreturn
declare void @llvm.dbg.declare(metadata, metadata, metadata) #4

declare dso_local i32 @AUTOSAR_GetCoreID() #1

declare dso_local void @AUTOSAR_StartCore(i32 noundef, i32* noundef) #1

declare dso_local void @AUTOSAR_StartOS(i32 noundef) #1

; Function Attrs: mustprogress noinline norecurse nounwind
define dso_local noundef i32 @main() #5 !dbg !74 {
entry:
  %retval = alloca i32, align 4
  store i32 0, i32* %retval, align 4
  %call = call i32 @AUTOSAR_GetCoreID(), !dbg !78
  %cmp = icmp eq i32 %call, 0, !dbg !78
  br i1 %cmp, label %if.then, label %if.end, !dbg !80

if.then:                                          ; preds = %entry
  store atomic i32 0, i32* @trace_table_idx seq_cst, align 4, !dbg !81
  store atomic i32 0, i32* @experiment_number seq_cst, align 4, !dbg !86
  store atomic i8 1, i8* @global_all_ok seq_cst, align 1, !dbg !87
  br i1 icmp ne (void ()* @test_prepare, void ()* null), label %if.then.i, label %_ZL9test_initv.exit, !dbg !88

if.then.i:                                        ; preds = %if.then
  call void @test_prepare() #7, !dbg !89
  br label %_ZL9test_initv.exit, !dbg !92

_ZL9test_initv.exit:                              ; preds = %if.then.i, %if.then
  br label %if.end, !dbg !93

if.end:                                           ; preds = %_ZL9test_initv.exit, %entry
  call void @_Z5startv(), !dbg !80
  %0 = load i32, i32* %retval, align 4, !dbg !80
  ret i32 %0, !dbg !80
}

; Function Attrs: alwaysinline mustprogress nounwind
define dso_local void @__OS_HOOK_DEFINED_ShutdownHook(i32 noundef %status) #0 !dbg !94 {
entry:
  %status.addr = alloca i32, align 4
  store i32 %status, i32* %status.addr, align 4
  call void @llvm.dbg.declare(metadata i32* %status.addr, metadata !97, metadata !DIExpression()), !dbg !98
  %call = call i32 @AUTOSAR_GetCoreID(), !dbg !99
  %cmp = icmp eq i32 %call, 1, !dbg !101
  br i1 %cmp, label %if.then, label %if.end, !dbg !102

if.then:                                          ; preds = %entry
  call void @test_trace_assert(i8* noundef getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i32 0, i32 0)), !dbg !103
  call void @test_finish(i32 noundef 0), !dbg !105
  br label %if.end, !dbg !106

if.end:                                           ; preds = %if.then, %entry
  ret void, !dbg !107
}

declare dso_local void @test_trace_assert(i8* noundef) #1

declare dso_local void @test_finish(i32 noundef) #1

declare extern_weak dso_local void @test_prepare() #1

attributes #0 = { alwaysinline mustprogress nounwind "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="cortex-a7" "target-features"="+armv7-a,+dsp,+hwdiv,+hwdiv-arm,+reserve-r9,+soft-float,+strict-align,+thumb-mode,-aes,-bf16,-cdecp0,-cdecp1,-cdecp2,-cdecp3,-cdecp4,-cdecp5,-cdecp6,-cdecp7,-crc,-crypto,-d32,-dotprod,-fp-armv8,-fp-armv8d16,-fp-armv8d16sp,-fp-armv8sp,-fp16,-fp16fml,-fp64,-fpregs,-fullfp16,-i8mm,-lob,-mve,-mve.fp,-neon,-pacbti,-ras,-sb,-sha2,-vfp2,-vfp2sp,-vfp3,-vfp3d16,-vfp3d16sp,-vfp3sp,-vfp4,-vfp4d16,-vfp4d16sp,-vfp4sp" "use-soft-float"="true" }
attributes #1 = { "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="cortex-a7" "target-features"="+armv7-a,+dsp,+hwdiv,+hwdiv-arm,+reserve-r9,+soft-float,+strict-align,+thumb-mode,-aes,-bf16,-cdecp0,-cdecp1,-cdecp2,-cdecp3,-cdecp4,-cdecp5,-cdecp6,-cdecp7,-crc,-crypto,-d32,-dotprod,-fp-armv8,-fp-armv8d16,-fp-armv8d16sp,-fp-armv8sp,-fp16,-fp16fml,-fp64,-fpregs,-fullfp16,-i8mm,-lob,-mve,-mve.fp,-neon,-pacbti,-ras,-sb,-sha2,-vfp2,-vfp2sp,-vfp3,-vfp3d16,-vfp3d16sp,-vfp3sp,-vfp4,-vfp4d16,-vfp4d16sp,-vfp4sp" "use-soft-float"="true" }
attributes #2 = { mustprogress noinline nounwind "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="cortex-a7" "target-features"="+armv7-a,+dsp,+hwdiv,+hwdiv-arm,+reserve-r9,+soft-float,+strict-align,+thumb-mode,-aes,-bf16,-cdecp0,-cdecp1,-cdecp2,-cdecp3,-cdecp4,-cdecp5,-cdecp6,-cdecp7,-crc,-crypto,-d32,-dotprod,-fp-armv8,-fp-armv8d16,-fp-armv8d16sp,-fp-armv8sp,-fp16,-fp16fml,-fp64,-fpregs,-fullfp16,-i8mm,-lob,-mve,-mve.fp,-neon,-pacbti,-ras,-sb,-sha2,-vfp2,-vfp2sp,-vfp3,-vfp3d16,-vfp3d16sp,-vfp3sp,-vfp4,-vfp4d16,-vfp4d16sp,-vfp4sp" "use-soft-float"="true" }
attributes #3 = { noreturn "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="cortex-a7" "target-features"="+armv7-a,+dsp,+hwdiv,+hwdiv-arm,+reserve-r9,+soft-float,+strict-align,+thumb-mode,-aes,-bf16,-cdecp0,-cdecp1,-cdecp2,-cdecp3,-cdecp4,-cdecp5,-cdecp6,-cdecp7,-crc,-crypto,-d32,-dotprod,-fp-armv8,-fp-armv8d16,-fp-armv8d16sp,-fp-armv8sp,-fp16,-fp16fml,-fp64,-fpregs,-fullfp16,-i8mm,-lob,-mve,-mve.fp,-neon,-pacbti,-ras,-sb,-sha2,-vfp2,-vfp2sp,-vfp3,-vfp3d16,-vfp3d16sp,-vfp3sp,-vfp4,-vfp4d16,-vfp4d16sp,-vfp4sp" "use-soft-float"="true" }
attributes #4 = { nofree nosync nounwind readnone speculatable willreturn }
attributes #5 = { mustprogress noinline norecurse nounwind "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="cortex-a7" "target-features"="+armv7-a,+dsp,+hwdiv,+hwdiv-arm,+reserve-r9,+soft-float,+strict-align,+thumb-mode,-aes,-bf16,-cdecp0,-cdecp1,-cdecp2,-cdecp3,-cdecp4,-cdecp5,-cdecp6,-cdecp7,-crc,-crypto,-d32,-dotprod,-fp-armv8,-fp-armv8d16,-fp-armv8d16sp,-fp-armv8sp,-fp16,-fp16fml,-fp64,-fpregs,-fullfp16,-i8mm,-lob,-mve,-mve.fp,-neon,-pacbti,-ras,-sb,-sha2,-vfp2,-vfp2sp,-vfp3,-vfp3d16,-vfp3d16sp,-vfp3sp,-vfp4,-vfp4d16,-vfp4d16sp,-vfp4sp" "use-soft-float"="true" }
attributes #6 = { noreturn }
attributes #7 = { nounwind }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!22, !23, !24, !25, !26, !27, !28, !29, !30}
!llvm.ident = !{!31}

!0 = distinct !DICompileUnit(language: DW_LANG_C_plus_plus_11, file: !1, producer: "Debian clang version 14.0.6", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !2, splitDebugInlining: false, nameTableKind: None)
!1 = !DIFile(filename: "../subprojects/ara/appl/AUTOSAR/multicore/minexample.cc", directory: "/mnt/d/Major_Project/parrot/build", checksumkind: CSK_MD5, checksum: "7aadd3da05c71fcbe5f13fc2e6b5c1a4")
!2 = !{!3}
!3 = !DICompositeType(tag: DW_TAG_enumeration_type, file: !4, line: 28, baseType: !5, size: 32, elements: !6, identifier: "_ZTS10StatusType")
!4 = !DIFile(filename: "subprojects/ara/libs/autosar/os/osek_types.h", directory: "/mnt/d/Major_Project/parrot", checksumkind: CSK_MD5, checksum: "4f531d5f34944f0eafd16b2ed9e8c39d")
!5 = !DIBasicType(name: "unsigned int", size: 32, encoding: DW_ATE_unsigned)
!6 = !{!7, !8, !9, !10, !11, !12, !13, !14, !15, !16, !17, !18, !19, !20, !21}
!7 = !DIEnumerator(name: "E_OK", value: 0, isUnsigned: true)
!8 = !DIEnumerator(name: "E_OS_ACCESS", value: 1, isUnsigned: true)
!9 = !DIEnumerator(name: "E_OS_CALLEVEL", value: 2, isUnsigned: true)
!10 = !DIEnumerator(name: "E_OS_ID", value: 3, isUnsigned: true)
!11 = !DIEnumerator(name: "E_OS_LIMIT", value: 4, isUnsigned: true)
!12 = !DIEnumerator(name: "E_OS_NOFUNC", value: 5, isUnsigned: true)
!13 = !DIEnumerator(name: "E_OS_RESOURCE", value: 6, isUnsigned: true)
!14 = !DIEnumerator(name: "E_OS_STATE", value: 7, isUnsigned: true)
!15 = !DIEnumerator(name: "E_OS_VALUE", value: 8, isUnsigned: true)
!16 = !DIEnumerator(name: "E_NOT_OK", value: 9, isUnsigned: true)
!17 = !DIEnumerator(name: "E_OS_CORE", value: 10, isUnsigned: true)
!18 = !DIEnumerator(name: "E_OS_SPINLOCK", value: 11, isUnsigned: true)
!19 = !DIEnumerator(name: "E_OS_NESTING_DEADLOCK", value: 12, isUnsigned: true)
!20 = !DIEnumerator(name: "E_OS_INTERFERENCE_DEADLOCK", value: 13, isUnsigned: true)
!21 = !DIEnumerator(name: "E_OS_MISSINGEND", value: 14, isUnsigned: true)
!22 = !{i32 7, !"Dwarf Version", i32 5}
!23 = !{i32 2, !"Debug Info Version", i32 3}
!24 = !{i32 1, !"wchar_size", i32 4}
!25 = !{i32 1, !"min_enum_size", i32 4}
!26 = !{i32 1, !"branch-target-enforcement", i32 0}
!27 = !{i32 1, !"sign-return-address", i32 0}
!28 = !{i32 1, !"sign-return-address-all", i32 0}
!29 = !{i32 1, !"sign-return-address-with-bkey", i32 0}
!30 = !{i32 7, !"frame-pointer", i32 2}
!31 = !{!"Debian clang version 14.0.6"}
!32 = distinct !DISubprogram(name: "AUTOSAR_ISR_Interrupt1", scope: !1, file: !1, line: 16, type: !33, scopeLine: 16, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!33 = !DISubroutineType(types: !34)
!34 = !{null}
!35 = !{}
!36 = !DILocation(line: 17, column: 5, scope: !32)
!37 = !DILocation(line: 18, column: 1, scope: !32)
!38 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskA", scope: !1, file: !1, line: 20, type: !33, scopeLine: 20, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!39 = !DILocation(line: 21, column: 5, scope: !38)
!40 = !DILocation(line: 22, column: 5, scope: !38)
!41 = !DILocation(line: 23, column: 1, scope: !38)
!42 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskB", scope: !1, file: !1, line: 25, type: !33, scopeLine: 25, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!43 = !DILocation(line: 26, column: 5, scope: !42)
!44 = !DILocation(line: 27, column: 5, scope: !42)
!45 = !DILocation(line: 28, column: 1, scope: !42)
!46 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskC", scope: !1, file: !1, line: 30, type: !33, scopeLine: 30, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!47 = !DILocation(line: 31, column: 5, scope: !46)
!48 = !DILocation(line: 32, column: 5, scope: !46)
!49 = !DILocation(line: 33, column: 1, scope: !46)
!50 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskD", scope: !1, file: !1, line: 35, type: !33, scopeLine: 35, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!51 = !DILocation(line: 36, column: 5, scope: !50)
!52 = !DILocation(line: 37, column: 5, scope: !50)
!53 = !DILocation(line: 38, column: 5, scope: !50)
!54 = !DILocation(line: 39, column: 1, scope: !50)
!55 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskE", scope: !1, file: !1, line: 41, type: !33, scopeLine: 41, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!56 = !DILocation(line: 42, column: 5, scope: !55)
!57 = !DILocation(line: 43, column: 5, scope: !55)
!58 = distinct !DISubprogram(name: "AUTOSAR_TASK_FUNC_TaskF", scope: !1, file: !1, line: 47, type: !33, scopeLine: 47, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!59 = !DILocation(line: 48, column: 5, scope: !58)
!60 = !DILocation(line: 49, column: 5, scope: !58)
!61 = !DILocation(line: 50, column: 5, scope: !58)
!62 = !DILocation(line: 51, column: 1, scope: !58)
!63 = distinct !DISubprogram(name: "start", linkageName: "_Z5startv", scope: !1, file: !1, line: 53, type: !33, scopeLine: 54, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!64 = !DILocalVariable(name: "rv", scope: !63, file: !1, line: 55, type: !65)
!65 = !DIDerivedType(tag: DW_TAG_typedef, name: "StatusType", file: !4, line: 44, baseType: !3)
!66 = !DILocation(line: 55, column: 16, scope: !63)
!67 = !DILocation(line: 56, column: 12, scope: !63)
!68 = !DILocation(line: 56, column: 5, scope: !63)
!69 = !DILocation(line: 58, column: 9, scope: !70)
!70 = distinct !DILexicalBlock(scope: !63, file: !1, line: 56, column: 25)
!71 = !DILocation(line: 60, column: 9, scope: !70)
!72 = !DILocation(line: 61, column: 5, scope: !70)
!73 = !DILocation(line: 62, column: 1, scope: !63)
!74 = distinct !DISubprogram(name: "main", scope: !1, file: !1, line: 64, type: !75, scopeLine: 64, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!75 = !DISubroutineType(types: !76)
!76 = !{!77}
!77 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!78 = !DILocation(line: 64, column: 1, scope: !79)
!79 = distinct !DILexicalBlock(scope: !74, file: !1, line: 64, column: 1)
!80 = !DILocation(line: 64, column: 1, scope: !74)
!81 = !DILocation(line: 249, column: 18, scope: !82, inlinedAt: !84)
!82 = distinct !DISubprogram(name: "test_init", linkageName: "_ZL9test_initv", scope: !83, file: !83, line: 247, type: !33, scopeLine: 247, flags: DIFlagPrototyped, spFlags: DISPFlagLocalToUnit | DISPFlagDefinition, unit: !0, retainedNodes: !35)
!83 = !DIFile(filename: "subprojects/ara/libs/autosar/test/test.h", directory: "/mnt/d/Major_Project/parrot", checksumkind: CSK_MD5, checksum: "26573ff48f958227399200edbda18823")
!84 = distinct !DILocation(line: 64, column: 1, scope: !85)
!85 = distinct !DILexicalBlock(scope: !79, file: !1, line: 64, column: 1)
!86 = !DILocation(line: 250, column: 20, scope: !82, inlinedAt: !84)
!87 = !DILocation(line: 251, column: 16, scope: !82, inlinedAt: !84)
!88 = !DILocation(line: 252, column: 6, scope: !82, inlinedAt: !84)
!89 = !DILocation(line: 253, column: 3, scope: !90, inlinedAt: !84)
!90 = distinct !DILexicalBlock(scope: !91, file: !83, line: 252, column: 25)
!91 = distinct !DILexicalBlock(scope: !82, file: !83, line: 252, column: 6)
!92 = !DILocation(line: 254, column: 2, scope: !90, inlinedAt: !84)
!93 = !DILocation(line: 64, column: 1, scope: !85)
!94 = distinct !DISubprogram(name: "__OS_HOOK_DEFINED_ShutdownHook", scope: !1, file: !1, line: 66, type: !95, scopeLine: 66, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !0, retainedNodes: !35)
!95 = !DISubroutineType(types: !96)
!96 = !{null, !65}
!97 = !DILocalVariable(name: "status", arg: 1, scope: !94, file: !1, line: 66, type: !65)
!98 = !DILocation(line: 66, column: 6, scope: !94)
!99 = !DILocation(line: 69, column: 9, scope: !100)
!100 = distinct !DILexicalBlock(scope: !94, file: !1, line: 69, column: 9)
!101 = !DILocation(line: 69, column: 21, scope: !100)
!102 = !DILocation(line: 69, column: 9, scope: !94)
!103 = !DILocation(line: 70, column: 9, scope: !104)
!104 = distinct !DILexicalBlock(scope: !100, file: !1, line: 69, column: 38)
!105 = !DILocation(line: 71, column: 9, scope: !104)
!106 = !DILocation(line: 72, column: 5, scope: !104)
!107 = !DILocation(line: 73, column: 1, scope: !94)
