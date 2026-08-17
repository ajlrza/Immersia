import * as os from 'os';
import Fastify from 'fastify';

export function getCPUStats(CPU_CHOICE: "good" | "normal" | "bad" | "extreme"): os.CpuInfo | undefined | os.CpuInfo[] {

    if (CPU_CHOICE == "good") {
        const good_cpu_time: os.CpuInfo | undefined = os.cpus().find(dict => (
            dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq >= 0
            && dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq <= 200
        ))
        return good_cpu_time
    }
    else if (CPU_CHOICE == "normal") {
        const normal_cpu_time: os.CpuInfo | undefined = os.cpus().find(dict => (
            dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq > 200
            && dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq <= 700
        ));
        return normal_cpu_time
    }
    else if (CPU_CHOICE == "bad") {
        const bad_cpu_time: os.CpuInfo | undefined = os.cpus().find(dict => (
            dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq > 700 
            && dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq <= 850
        ));
        return bad_cpu_time
    }
    else if (CPU_CHOICE == "extreme") {
        const extreme_cpu_time: os.CpuInfo | undefined = os.cpus().find(
            dict => (dict.times.user + dict.times.nice + dict.times.sys + dict.times.irq > 850
        ));
        return extreme_cpu_time
    }
    else {
        const cpuGeneralList: os.CpuInfo[] = os.cpus()
        return cpuGeneralList
    }
    
}