#!/usr/bin/env ruby
#
# automatically created by Dojo Polyglot Environ on 2011-12-09 19:54:15
# https://github.com/afurlan/dojo-polyglot-environ

require "test/unit"

class Estatistica
   
    attr_accessor :vetor

    def initialize
      @vetor = []
    end

    def add_vetor(elementos)
        elementos.each do |i| @vetor.push(i)
        end 
    end

    def add_elemento(elemento)
        @vetor.push(elemento)
    end
end

class Testestatistica < Test::Unit::TestCase
    def test_initialize
        assert_not_nil(Estatistica.new)
    end
    def test_vetor_deve_iniciar_vazia
        estatistica = Estatistica.new
        assert(estatistica.vetor.empty?)
    end
    def test_vetor1_dever_retornar1
        estatistica = Estatistica.new
        estatistica.add_elemento(1)
        assert_equal(estatistica.vetor.length,1)    
    end
    def test_vetor2_deve_retornar2
        estatistica = Estatistica.new
        estatistica.add_elemento(1)
        estatistica.add_elemento(1)
        assert_equal(estatistica.vetor.length,2)
    end
    def test_inicializar_com_vetor
        estatistica = Estatistica.new
        estatistica.add_vetor([1,2,3])
        assert_equal(estatistica.vetor.length, 3)
    end
    
        
end

